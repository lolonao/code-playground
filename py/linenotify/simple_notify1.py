import requests

LINE_NOTIFY_TOKEN = "uzGHMbOhqza0RUuNKwdfKXv2kc714DEJCVzFrDUXIMP"
message = "message"

url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": "Bearer"+LINE_NOTIFY_TOKEN}
payload = {"message": message}

r = requests.post(url, headers=headers, params=payload)

print(r)

