import requests


# 発行された LINE Notifyトークン
LINE_NOTIFY_TOKEN = "uzGHMbOhqza0RUuNKwdfKXv2kc714DEJCVzFrDUXIMP"

def send_line(msg):
    #サーバーに送るパラメータを用意
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + LINE_NOTIFY_TOKEN}
    payload = {'message': msg}

    #requestsモジュールのpost関数を利用してメッセージを送信する
    #ヘッダにトークン情報，パラメータにメッセージを指定する
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    #メッセージを送信
    send_line('Hello, world!')
    print('OK')
