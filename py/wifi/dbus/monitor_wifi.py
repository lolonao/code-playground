#!/usr/bin/env python3
"""
monitor_wifi.py
---------------
・DBus (SystemBus) を経由して ConnMan の Wi-Fi サービス一覧を取得
・事前に「設定ファイル or connmanctl connect」で登録済みの
  Wi-Fi ネットワークだけを監視対象とする
・10 秒ごとに取得し、前回との差分があれば標準出力へ通知
・外部コマンドを一切使わないので負荷が低い
"""

import time
import dbus
from typing import Set

# ----------------------------------------------------------
# 監視したい Wi-Fi サービス ID のリスト
# 例: 隠しネット / 通常ネット混在可
TARGET_SERVICES: Set[str] = {
    "wifi_1c1bb5e40be7_4f524f20576966692056656e646f_managed_none",
    "wifi_1c1bb5e40be7_44454c454c414e47434f4e4e454354_managed_psk",
    "wifi_dc85de828967_68756773616d_managed_psk",
}


# ----------------------------------------------------------
def get_wifi_service_ids() -> Set[str]:
    """
    ConnMan から現在 Available な Wi-Fi サービスの DBus path
    の末尾部分（= service ID）を集合で返す。
    """
    bus = dbus.SystemBus()
    # Manager オブジェクトを取得
    manager = dbus.Interface(bus.get_object("net.connman", "/"), "net.connman.Manager")

    services = manager.GetServices()  # キャッシュが返るので高速
    wifi_ids = set()
    for path, props in services:
        # Type が "wifi" だけを対象
        if props.get("Type") == "wifi":
            # path は "/net/connman/service/xxxxxxxx"
            service_id = path.split("/")[-1]
            wifi_ids.add(service_id)
    return wifi_ids


# ----------------------------------------------------------
def main() -> None:
    """
    メインループ：10 秒毎に取得し、TARGET_SERVICES の出現／消失を検知
    """
    previous: Set[str] = set()

    while True:
        try:
            current = get_wifi_service_ids()
            # 監視対象のうち「現れた」「消えた」ものだけ抽出
            appeared = TARGET_SERVICES & current - previous
            disappeared = TARGET_SERVICES & previous - current

            for sid in appeared:
                print(f"[+] appeared : {sid}")
            for sid in disappeared:
                print(f"[-] disappeared : {sid}")

            previous = current
        except Exception as e:
            # 通信エラー時はエラーメッセージを出して次へ
            print(f"Error: {e}")

        time.sleep(10)


# ----------------------------------------------------------
if __name__ == "__main__":
    main()

