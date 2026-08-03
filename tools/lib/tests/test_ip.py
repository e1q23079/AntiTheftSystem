from unittest import TestCase
from unittest.mock import MagicMock

from fastapi import Request
from lib.ip import get_client_ip


class TestIP(TestCase):
    """
    IPクラスのテストケース
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        self.request = MagicMock(spec=Request)
        self.origin_request = self.request

    def tearDown(self):
        """
        テストの後処理
        """
        self.request = self.origin_request

    def test_get_client_ip_success(self):
        """
        get_client_ip関数のテスト（クライアントIPが取得できる場合）
        """
        # クライアントIPが取得できる場合のテスト
        self.request.client = MagicMock()
        self.request.client.host = "192.168.1.1"
        self.assertEqual(get_client_ip(self.request), "192.168.1.1")

    def test_get_client_ip_none(self):
        """
        get_client_ip関数のテスト（クライアントIPが取得できない場合）
        """
        # クライアントIPが取得できない場合のテスト
        self.request.client = None
        self.assertIsNone(get_client_ip(self.request))
