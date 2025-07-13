#!/usr/bin/env python3
"""
monitor_wifi_with_ssid.py
-------------------------
・DBus(SystemBus)経由で登録済み Wi-Fi サービス一覧を取得
・10 秒ごとに差分をチェック
・「service ID」と「SSID」をペアで表示
"""

import time
import dbus
from typing import Dict, Set

# 監視対象の service ID（省略時は全件）
WATCH_LIST: Set[str] = {
    "wifi_1c1bb5e40be7_4f524f20576966692056656e646f_managed_none",
    "wifi_1c1bb5e40be7_44454c454c414e47434f4e4e454354_managed_psk",
}

def get_wifi_services_with_ssid() -> Dict[str, str]:
    """
    現在 Available な Wi-Fi サービスの
    {service_id: ssid} 辞書を返す。
    """
    bus = dbus.SystemBus()
    manager = dbus.Interface(
        bus.get_object("net.connman", "/"),
        "net.connman.Manager"
    )

    services = manager.GetServices()
    result: Dict[str, str] = {}
    for path, props in services:
        if props.get("Type") != "wifi":
            continue

        service_id = path.split("/")[-1]
        # props["Name"] が存在しない場合は "(SSID不明)" にフォールバック
        ssid = str(props.get("Name", "(SSID不明)"))
        result[service_id] = ssid
    return result

def main() -> None:
    prev: Dict[str, str] = {}

    while True:
        try:
            curr = get_wifi_services_with_ssid()

            # 監視対象を絞る（WATCH_LIST が空なら全件）
            if WATCH_LIST:
                curr = {k: v for k, v in curr.items() if k in WATCH_LIST}

            # 差分計算
            appeared   = {k: curr[k] for k in curr.keys() - prev.keys()}
            disappeared = {k: prev[k] for k in prev.keys() - curr.keys()}

            for sid, ssid in appeared.items():
                print(f"[+] appeared : {sid}  ({ssid})")
            for sid, ssid in disappeared.items():
                print(f"[-] disappeared : {sid}  ({ssid})")

            prev = curr
        except Exception as e:
            print("Error:", e)

        time.sleep(10)

if __name__ == "__main__":
    main()

