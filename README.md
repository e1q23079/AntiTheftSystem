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

## 2. M5側のプログラムの書き方

M5側のプログラムは、Arduino / PlatformIO の基本構成に従って `setup()` と `loop()` で実装します。

- `setup()`: デバイス起動時に1回実行される初期化処理です。
  - `M5.begin()` で M5 デバイスを初期化します。
  - `Serial.begin()` でシリアル通信を開始します。
  - Wi-Fi の設定や接続を行います。
  - `antiTheftSystem.begin()` で盗難防止システムを起動します。
- `loop()`: 起動後に繰り返し実行される処理です。
  - ここでは待機処理を行い、必要に応じてセンサー監視や通知処理を追加します。

以下は基本的な記述例です。

```cpp
#include <AntiTheftSystem.h>
#include <M5unified.h>

#include "setting/setting.h"

AntiTheftSystem antiTheftSystem(SERVER_URL);

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);

    Serial.begin(115200);

    antiTheftSystem.configureWiFi(IP_ADDRESS, GATEWAY_IP, SUBNET_MASK);
    antiTheftSystem.connectToWiFi(WIFI_SSID, WIFI_PASSWORD);

    antiTheftSystem.setDebugMode(true); // デバッグモードを有効にする
    antiTheftSystem.begin();
}

void loop() {
    delay(1000);
}
```

## 3. プログラムのビルドと書き込み

### M5StickC Plus / M5StickC Plus2

対応するデバイス名は次のとおりです。

- `m5stick-c`
- `m5stick-s3`
- `m5stack-cores3`

以下のコマンドでビルドと書き込みを行います。

```bash
pio run -e <デバイス名> -t upload
```

### 3.1 ライブラリとして使う場合

このライブラリは、別の PlatformIO プロジェクトから `lib_deps` で追加できます。

```ini
lib_deps =
  m5stack/M5Unified@^0.2.17
  https://github.com/e1q23079/AntiTheftSystem.git
```

追加後は、次のように利用できます。

```cpp
#include <AntiTheftSystem.h>

AntiTheftSystem antiTheftSystem(SERVER_URL);
```

## 4. 監視システムのセットアップ

### 4.1 環境構築

監視システム用の設定ファイルは `tools/.env` です。

```py
WEB_HOOK_URL="webhook_url"
```

次のコマンドで仮想環境を作成します。

```bash
cd tools/
python -m venv .venv
```

### 4.2 プログラムの実行

Windows では、次のコマンドで仮想環境を有効化します。

```bash
.venv\Scripts\activate
```

その後、以下で監視システムを起動します。

```bash
python main.py
```

実行を停止する場合は `Ctrl + C` を入力してください。

## 5. APIエンドポイント

<http://localhost:8000/docs>

この監視システムは FastAPI で動作し、M5 デバイスからのアクセスを受けて状態を更新します。主な API は次の 2 つです。

### `GET /api/v1/check`

現在アクセスしてきたデバイスの IP アドレスをもとに、そのデバイスの稼働状態を `true` として更新します。M5 デバイス側から定期的に呼び出すことで、「端末が生存している」ことを監視側へ通知する用途です。

返却値は次のとおりです。

```json
{
  "status": true
}
```

### `GET /api/v1/get/devices`

登録済みデバイスの一覧を取得します。各デバイスについて、名前、IP アドレス、現在の状態、通知済みフラグを確認できます。監視画面やデバッグ時の確認に使用します。

返却値の例は次のとおりです。

```json
{
  "devices": [
    {
      "name": "M5StickC Plus",
      "ip": "192.168.4.9",
      "status": false,
      "notified": true
    },
    {
      "name": "M5StickC Plus 2",
      "ip": "192.168.4.8",
      "status": false,
      "notified": true
    },
    {
      "name": "M5Stick S3",
      "ip": "192.168.4.7",
      "status": false,
      "notified": true
    },
    {
      "name": "M5Stack S3",
      "ip": "192.168.4.6",
      "status": false,
      "notified": true
    },
    {
      "name": "M5Stack S3 SE",
      "ip": "192.168.4.5",
      "status": false,
      "notified": true
    }
  ]
}
```
