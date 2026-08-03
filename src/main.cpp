#include <AntiTheftSystem.h>
#include <M5unified.h>

#include "setting/setting.h"

AntiTheftSystem antiTheftSystem(SERVER_URL);

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);

    Serial.begin(115200);
    Serial.println("M5 Starting...");

    M5.Display.fillScreen(WHITE);

    antiTheftSystem.configureWiFi(IP_ADDRESS, GATEWAY_IP, SUBNET_MASK);
    antiTheftSystem.connectToWiFi(WIFI_SSID, WIFI_PASSWORD);

    antiTheftSystem.setDebugMode(true);  // デバッグモードを有効化

    antiTheftSystem.begin();  // 盗難防止システム作動
}

void loop() { delay(1000); }