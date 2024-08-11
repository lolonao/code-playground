"""
[Raspberry pi pico W と 秋月電子通商 AE-ESP32-WROOM-32E-MINI の消費電流を比較](https://blog.masasoft.jp/2024/05/raspberry-pi-pico-w-ae-esp32-wroom-32e.html)
起動、LED点滅(2回)、1秒 sleep、WiFi に接続、接続したらLED点滅(3回)、http アクセス、1秒 sleep、LED点滅(1回)、deepsleep(10秒) を繰り返すプログラム
"""

import network
import urequests as requests
from time import sleep
from machine import Pin, deepsleep

# WiFi ssid and password
ssid = '0024A50722AC'
password = '3w4p127sv8rp9'

wlan_status_message = {
    network.STAT_IDLE: 'No connection and no activity',
    network.STAT_CONNECTING: 'Connecting in progress',
    network.STAT_WRONG_PASSWORD: 'Failed due to incorrect password',
    network.STAT_NO_AP_FOUND: 'Failed because no access point replied',
#    network.STAT_CONNECT_FAIL: 'failed due to other problems',
    network.STAT_GOT_IP: 'Connection successful'
}

def get_wlan_status_message(wlan_status):
    if wlan_status in wlan_status_message:
        return wlan_status_message[wlan_status]
    else:
        return str(wlan_status)

# Define blinking function for onboard LED to indicate error codes    
def blink_led(num_blinks):
    led = Pin(15, Pin.OUT)
    if num_blinks < 0:
        num_blinks = 8 + num_blinks
    for i in range(num_blinks):
        led.on()
        sleep(.2)
        led.off()
        sleep(.2)

try:
    blink_led(2)
    # Print the last result
    with open('result.txt') as f:
        print('last result:', f.read())

    sleep(1)
    
    # Turn on WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0 and not wlan.isconnected():
        print('wlan: connecting')
        sleep(1)
        max_wait -= 1
        
    # Handle connection error
    wlan_status = wlan.status()
    if wlan_status == network.STAT_GOT_IP:
        print('wlan: connected')
        blink_led(3)
        status = wlan.ifconfig()
        print('ip = ' + status[0])
    else:
        blink_led(5)
        raise Exception(get_wlan_status_message(wlan_status))

    # Send information to the web server
    url = 'http://raspi1.home/updatestate.php?mail'
    print('request:', url)
    res = requests.get(url)
    print('response:', res.text)
    with open('result.txt', 'w') as f:
        f.write(res.text)
    res.close()
    
    wlan.disconnect()
    wlan.active(False)


except Exception as e:
    print('error:', str(e))
    with open('result.txt', 'w') as f:
        f.write(str(e))
except KeyboardInterrupt:
    print('Interrupted!')    
        
# Go to deep sleep
sleep(1)
blink_led(1)
s = Pin(13, Pin.IN, Pin.PULL_UP)
if s.value() == 1:  # If GPIO13 is open (not connected to GND), fall in to deep sleep
    print('Fall in deep sleep')
    deepsleep(10 * 1000)
else:
    print('End')

