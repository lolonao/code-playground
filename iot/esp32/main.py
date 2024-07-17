from time import sleep, localtime
import machine
import network
import urequests
import ujson


def blink_led():
    pin12 = machine.Pin(2, machine.Pin.OUT)
    for i in range(10):
        pin12.on()
        sleep(0.1)
        pin12.off()
        sleep(0.1)


def network_check():
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    scan_result = sta_if.scan()
    # Scan for available access points
    print(f"スキャン結果: {scan_result}")
    # Connect to an AP
    sta_if.connect("Globe_LTE_MIFI_E55F", "60105043")
    sleep(3)
    # Check for successful connection
    print(f"接続中か？: {sta_if.isconnected()}")


def print_now():
    now = localtime()
    print("現在時刻は {}-{}-{} {}:{}:{}".format(
        now[0], now[1], now[2], now[3], now[4], now[5]))

def connect_to_wifi():
    # ネットワーク名とパスワードを設定します。
    network_name = "SKYW_A7A2_2G"
    network_password = "vNNqJ7Qk"

    # Wi-Fi に接続します。
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(network_name, network_password)

    # Wi-Fi に接続されるまで待ちます。
    while not wifi.isconnected():
        pass

    print("ネットワーク接続成功！")
    return wifi


def get_exchange_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = urequests.get(url)
    data = ujson.loads(response.content)
    exchange_rate = data['rates']['JPY']
    return exchange_rate


def get_exchange_rate2():
    url = 'https://api.exchangerate-api.com/v4/latest/PHP'
    response = urequests.get(url)
    data = ujson.loads(response.content)
    exchange_rate = data['rates']['JPY']
    return exchange_rate


def get_crypto_exchange_rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = urequests.get(url)
    data = ujson.loads(response.content)
    exchange_rate = data['bpi']['USD']['rate']
    return exchange_rate


def hoge():
    # 現在の BTC / USD レートを取得します。
    response = urequests.get("https://api.coinmarketcap.com/v2/ticker/bitcoin/?convert=USD")
    rates = response.json()["data"]["quotes"]["USD"]["price"]
    print("現在の BTC/USD レートは 1 BTC = {} USD です".format(rates))


def hoge2():
    # 現在の BTC / USD レートを取得します。
    response = urequests.get("https://api.coinmarketcap.com/v2/ticker/bitcoin/?convert=USD")
    rates = response.json()["data"]["quotes"]["USD"]["price"]
    print("現在の BTC/USD レートは 1 BTC = {} USD です".format(rates))
    

def print_version():
    version: str = "1.0"
    print("\n---------------------------")
    print(f"Show Exchange Rates Ver {version}")
    print("---------------------------\n")


def main():
    try:
        wifi = connect_to_wifi()
        print("May be connected done!")

        exchange_rate = get_exchange_rate()
        print("JPY/USD exchange rate: ", exchange_rate)
        #print("現在の JPY/USD レートは 1 USD = {} JPY です".format(rates["JPY"]))
        exchange_rate = get_exchange_rate2()
        print("PHP/JPY exchange rate: ", exchange_rate)

        exchange_rate = get_crypto_exchange_rate()
        print("BTC/USD exchange rate: ", exchange_rate)
        
        print("ネットワークを切断")
        wifi.disconnect()

    except Exception as e:
        print("ネットワークを切断")
        wifi.disconnect()
        print(f"エラー: {e}")

    
if __name__ == "__main__":
    print_version()
    while True:
        print_now()
        blink_led()
        main()
        print("=========")
        sleep(60 * 1)  # 10分待機

## OSError: Wifi Internal Error が発生しないよう例外処理をする


