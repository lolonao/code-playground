import urequests
import ujson

def get_exchange_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/JPY'
    response = urequests.get(url)
    data = ujson.loads(response.content)
    exchange_rate = data['rates']['USD']
    return exchange_rate

def main():
    exchange_rate = get_exchange_rate()
    print("JPY/USD exchange rate: ", exchange_rate)

main()



