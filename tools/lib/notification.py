import requests


def send_notification(title, message, webhook_url) -> bool:
    """
    DiscordのWebhookを使用して通知を送信する関数
    Args:
        title (str): 通知のタイトル
        message (str): 通知のメッセージ
        webhook_url (str): DiscordのWebhook URL
    """
    data = {"content": f"**{title}**\n{message}"}
    response = requests.post(webhook_url, json=data)
    return response.status_code == 204
