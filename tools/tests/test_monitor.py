from unittest import TestCase
from unittest.mock import MagicMock, patch

from server.monitor import monitor_loop


class TestMonitor(TestCase):
    """
    モニタリング機能のテストケース
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        self.mock_devices = MagicMock()
        self.webhook_url = "https://example.com/webhook"

    @patch("server.monitor.send_notification")
    @patch("time.sleep")
    def test_monitor_loop(self, mock_sleep, mock_send_notification):
        """
        monitor_loop関数のテスト
        """
        mock_sleep.return_value = None  # time.sleepを無効化
        # デバイスの状態を設定
        self.mock_devices.get_devices.side_effect = [
            [
                {
                    "name": "デバイスA",
                    "ip": "192.168.1.1",
                    "status": True,
                    "notified": False,
                },
                {
                    "name": "デバイスB",
                    "ip": "192.168.1.2",
                    "status": False,
                    "notified": False,
                },
                {
                    "name": "デバイスC",
                    "ip": "192.168.1.3",
                    "status": False,
                    "notified": True,
                },
            ],
            KeyboardInterrupt(),  # ループを終了させるためにKeyboardInterruptを発生させる
        ]

        with self.assertRaises(KeyboardInterrupt):
            monitor_loop(self.webhook_url, self.mock_devices)

            mock_send_notification.assert_called_once_with(
                "デバイス接続状態の通知",
                "デバイス デバイスB (192.168.1.2) が接続されていません。",
                self.webhook_url,
            )

            self.mock_devices.update_device_notified.assert_called_once_with(
                "192.168.1.2", True
            )
