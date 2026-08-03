# デバイス盗難防止システム

このプロジェクトは、M5デバイスと監視システムを組み合わせて、端末の盗難を検知し、通知する仕組みです。

## 1. M5デバイスの設定

設定ファイルは `src/setting/setting.h` です。

以下のように必要な項目を設定してください。

```c++
// Sample setting.h file for M5SesameUDPModule project

# define IP_ADDRESS "192.168.1.50"

# define WIFI_SSID "your-ssid"

# define WIFI_PASSWORD "your-password"

# define GATEWAY_IP "192.168.1.1"

# define SUBNET_MASK "255.255.255.0"

# define SERVER_URL "http://192.168.1.1:8000"
```

設定項目の概要は次のとおりです。

- `IP_ADDRESS`: デバイスの IP アドレス
- `WIFI_SSID`: 接続する Wi-Fi の SSID
- `WIFI_PASSWORD`: Wi-Fi のパスワード
- `GATEWAY_IP`: ゲートウェイ IP
- `SUBNET_MASK`: サブネットマスク
- `SERVER_URL`: 監視サーバーの URL

## 2. プログラムのビルドと書き込み

### M5StickC Plus / M5StickC Plus2

対応するデバイス名は次のとおりです。

- `m5stick-c`
- `m5stick-s3`
- `m5stack-cores3`

以下のコマンドでビルドと書き込みを行います。

```bash
pio run -e <デバイス名> -t upload
```

## 3. 監視システムのセットアップ

### 3.1 環境構築

監視システム用の設定ファイルは `tools/.env` です。

```py
WEB_HOOK_URL="webhook_url"
```

次のコマンドで仮想環境を作成します。

```bash
cd tools/
python -m venv .venv
```

### 3.2 プログラムの実行

Windows では、次のコマンドで仮想環境を有効化します。

```bash
.venv\Scripts\activate
```

その後、以下で監視システムを起動します。

```bash
python main.py
```

実行を停止する場合は `Ctrl + C` を入力してください。
