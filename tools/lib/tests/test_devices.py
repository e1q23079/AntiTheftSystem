from unittest import TestCase

from lib.devices import Devices


class TestDevices(TestCase):
    """
    Devicesクラスのテストケース
    """

    def setUp(self):
        """
        テスト用のデバイスリストを初期化する
        """
        self.devices_list = [
            {"ip": "192.168.1.1"},
            {"ip": "192.168.1.2"},
            {"ip": "192.168.1.3"},
        ]
        self.devices = Devices(self.devices_list)

    def test_update_device_status(self):
        """
        デバイスの接続状態を更新するメソッドのテスト
        """
        self.devices.update_device_status("192.168.1.1", True)
        self.assertTrue(self.devices.devices[0]["status"])

    def test_update_device_notified(self):
        """
        デバイスの通知状態を更新するメソッドのテスト
        """
        self.devices.update_device_notified("192.168.1.1", True)
        self.assertTrue(self.devices.devices[0]["notified"])

    def test_reset_device_status(self):
        """
        すべてのデバイスの接続状態をリセットするメソッドのテスト
        """
        self.devices.update_device_status("192.168.1.1", True)
        self.devices.reset_device_status()
        for device in self.devices.devices:
            self.assertFalse(device["status"])

    def test_get_devices(self):
        """
        デバイスのリストを取得するメソッドのテスト
        """
        devices = self.devices.get_devices()
        self.assertEqual(devices, self.devices_list)
