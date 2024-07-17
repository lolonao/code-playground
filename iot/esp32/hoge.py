
"""
MicroPython v1.19.1 on 2022-06-18; 4MB/OTA module with ESP32
Type "help()" for more information.
>>> help
<function>
>>> help()
Welcome to MicroPython on the ESP32!

For generic online docs please visit http://docs.micropython.org/

For access to the hardware use the 'machine' module:
"""

import machine
from time import sleep

pin12 = machine.Pin(2, machine.Pin.OUT)
pin12.value(1)
sleep(2)
pin12.off()

"""
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
i2c.writeto(addr, b'1234')
i2c.readfrom(addr, 4)
"""

# Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
scan_result = sta_if.scan()
print(f"スキャン結果: {scan_result}") # Scan for available access points
sta_if.connect("Globe_LTE_MIFI_E55F", "60105043") # Connect to an AP
sleep(3)
print(f"接続中か？: {sta_if.isconnected()}")                      # Check for successful connection

"""
Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
"""

