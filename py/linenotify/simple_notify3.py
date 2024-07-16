import requests


# 発行された LINE Notifyトークン
LINE_NOTIFY_TOKEN = "uzGHMbOhqza0RUuNKwdfKXv2kc714DEJCVzFrDUXIMP"

def send_line(msg):
    """LINE Notifyへメッセージを送信する関数

    Args:
        msg (str): 送信するメッセージ

    """
    try:
        # サーバーに送るパラメータを用意
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + LINE_NOTIFY_TOKEN}
        payload = {'message': msg}

        # requestsモジュールのpost関数を利用してメッセージを送信する
        # ヘッダにトークン情報，パラメータにメッセージを指定する
        requests.post(url, headers=headers, params=payload)

        print('LINE Notifyへメッセージを送信しました:', msg)
    except Exception as e:
        # エラーが発生した場合、エラー内容をLINE Notifyで通知する
        error_msg = f'LINE Notifyへのメッセージ送信中にエラーが発生しました: {e}'
        send_line(error_msg)
        raise e


if __name__ == '__main__':
    # メッセージを送信
    send_line('暗号資産情報')
