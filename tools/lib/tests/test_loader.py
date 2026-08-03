from unittest import TestCase
from unittest.mock import mock_open, patch

from lib.loader import Loader


class TestLoader(TestCase):
    """
    Loaderクラスのテストケース
    """

    @patch(
        "lib.loader.open",
        new_callable=mock_open,
        read_data='[{"name": "デバイスA", "ip": "192.168.1.2"}]',
    )
    def test_load_devices(self, mock_open):
        """
        デバイス情報のロードテスト
        """
        loader = Loader("tests/test_data/devices.json")
        devices = loader.get_devices()
        self.assertIsNotNone(devices)
        if devices is not None:
            self.assertEqual(len(devices), 1)
            self.assertEqual(devices[0]["name"], "デバイスA")
            self.assertEqual(devices[0]["ip"], "192.168.1.2")

    @patch("lib.loader.open", new_callable=mock_open, read_data="invalid json")
    def test_load_devices_file_not_found(self, mock_open):
        """
        ファイルが存在しない場合のテスト
        """
        mock_open.side_effect = FileNotFoundError
        loader = Loader("tests/test_data/non_existent_file.json")
        devices = loader.get_devices()
        self.assertIsNone(devices)

    @patch("lib.loader.open", new_callable=mock_open, read_data="invalid json")
    def test_load_devices_invalid_json(self, mock_open):
        """
        JSON形式が不正な場合のテスト
        """
        loader = Loader("tests/test_data/invalid_json.json")
        devices = loader.get_devices()
        self.assertIsNone(devices)
