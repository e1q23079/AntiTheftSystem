from unittest import TestCase
from unittest.mock import patch

from lib.notification import send_notification


class TestNotification(TestCase):
    """
    Notificationクラスのテストケース
    """

    @patch("lib.notification.requests.post")
    def test_send_notification(self, mock_post):
        """
        DiscordのWebhookを使用して通知を送信するテスト（成功ケース）
        """
        title = "テスト通知"
        message = "これはテストメッセージです。"
        webhook_url = "https://discord.com/api/webhooks/your_webhook_url"

        # モックのレスポンスを設定
        mock_post.return_value.status_code = 204

        # 通知を送信
        result = send_notification(title, message, webhook_url)

        # 送信結果を検証
        self.assertTrue(result)

    def test_send_notification_failure(self):
        """
        DiscordのWebhookを使用して通知を送信するテスト（失敗ケース）
        """
        title = "テスト通知"
        message = "これはテストメッセージです。"
        webhook_url = "https://discord.com/api/webhooks/your_webhook_url"

        # モックのレスポンスを設定
        with patch("lib.notification.requests.post") as mock_post:
            mock_post.return_value.status_code = 400

            # 通知を送信
            result = send_notification(title, message, webhook_url)

            # 送信結果を検証
            self.assertFalse(result)
