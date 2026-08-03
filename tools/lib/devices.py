class Devices:
    """
    デバイスのリストを管理するクラス
    Attributes:
        devices (list): デバイスのリスト
    """

    def __init__(self, devices):
        """
        Args:
            devices (list): デバイスのリスト
        """
        self.devices: list = devices
        for device in self.devices:
            device["status"] = False
            device["notified"] = False

    def update_device_status(self, device_ip, status):
        """
        デバイスの接続状態を更新するメソッド
        Args:
            device_ip (str): デバイスのIPアドレス
            status (bool): デバイスの接続状態
        """
        for device in self.devices:
            if device["ip"] == device_ip:
                device["status"] = status
                break

    def update_device_notified(self, device_ip, notified):
        """
        デバイスの通知状態を更新するメソッド
        Args:
            device_ip (str): デバイスのIPアドレス
            notified (bool): デバイスの通知状態
        """
        for device in self.devices:
            if device["ip"] == device_ip:
                device["notified"] = notified
                break

    def reset_device_status(self):
        """
        すべてのデバイスの接続状態をリセットするメソッド
        """
        for device in self.devices:
            device["status"] = False

    def get_devices(self):
        """
        デバイスのリストを取得するメソッド
        Returns:
            list: デバイスのリスト
        """
        return self.devices
