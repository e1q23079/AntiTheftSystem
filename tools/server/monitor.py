import logging
import time

from lib.devices import Devices
from lib.notification import send_notification

logger = logging.getLogger(__name__)

first_run = True  # 初回実行フラグ


def monitor_loop(webhook_url: str, devices: Devices):
    """
    デバイスの接続状態を監視するループ関数
    """
    global first_run
    while True:
        if first_run:
            logger.info("Waiting for 30 seconds before starting the server...")
            time.sleep(30)  # アクセスが来ていない可能性が高いため，はじめ30秒は待機する
            logger.info("Starting the monitoring loop...")
            first_run = False
        devices_list = devices.get_devices()
        for device in devices_list:
            if not device["status"] and not device["notified"]:
                # デバイスが接続されていない場合、通知を送信
                title = "デバイス接続状態の通知"
                message = (
                    f"デバイス {device['name']} ({device['ip']}) が接続されていません。"
                )
                send_notification(title, message, webhook_url)
                devices.update_device_notified(device["ip"], True)
            elif device["status"] and device["notified"]:
                # デバイスが再接続された場合、通知状態をリセット
                devices.update_device_notified(device["ip"], False)
        devices.reset_device_status()  # すべてのデバイスの接続状態をリセット
        time.sleep(15)  # 15秒ごとに状態をチェック
