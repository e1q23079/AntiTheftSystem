from unittest import TestCase
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient
from server.server import app


class TestAPI(TestCase):
    """
    APIのテストケース
    """

    def setUp(self):
        self.mock_devices = MagicMock()
        app.state.devices = self.mock_devices
        self.client = TestClient(app)

    def test_check_endpoint(self):
        """
        /api/v1/checkエンドポイントのテスト
        """
        with patch("server.server.get_client_ip", return_value="192.168.1.1"):
            response = self.client.get("/api/v1/check")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"status": True})
            self.mock_devices.update_device_status.assert_called_once_with(
                "192.168.1.1", True
            )

    def test_get_devices_endpoint(self):
        """
        /api/v1/get/devicesエンドポイントのテスト
        """
        self.mock_devices.get_devices.return_value = [
            {"name": "デバイスA", "ip": "192.168.1.1"}
        ]
        with patch("server.server.get_client_ip", return_value="192.168.1.1"):
            response = self.client.get("/api/v1/get/devices")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"devices": [{"name": "デバイスA", "ip": "192.168.1.1"}]},
            )
            self.mock_devices.get_devices.assert_called_once()
