import json


class Loader:
    """
    デバイス情報をJSONファイルから読み込むクラス
    Attributes:
        file_path (str): JSONファイルのパス
        json_data (dict | None): 読み込んだJSONデータ
    """

    def __init__(self, file_path: str):
        """
        Args:
            file_path (str): JSONファイルのパス
        """
        self.file_path = file_path
        self.json_data = self._load()

    def _load(self) -> dict | None:
        """
        JSONファイルを読み込む内部メソッド
        Returns:
            dict | None: 読み込んだJSONデータ。ファイルが存在しない場合やJSONの形式が不正な場合はNoneを返す。
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None

    def get_devices(self) -> dict | None:
        """
        読み込んだJSONデータを返すメソッド
        Returns:
            dict | None: 読み込んだJSONデータ。ファイルが存在しない場合やJSONの形式が不正な場合はNoneを返す。
        """
        return self.json_data
