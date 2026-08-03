#include "AntiTheftSystem.h"

AntiTheftSystem::AntiTheftSystem(const char* server_url)
    : server_url(server_url) {}

void AntiTheftSystem::monitorTask(void* arg) {
    auto* self = static_cast<AntiTheftSystem*>(arg);
    self->monitorDevices();
}

void AntiTheftSystem::notifyWarning() {
    M5.Speaker.tone(2000, 500);
    M5.Display.fillScreen(RED);
}

void AntiTheftSystem::monitorDevices() {
    Serial.println("Monitoring devices...");
    while (true) {
        if (WiFi.isConnected()) {
            if (debug) {
                M5.Display.fillScreen(GREEN);
            }
            if (check_counter == 10) {  // 10秒ごとにサーバーにアクセス
                getCheckAPI();
                check_counter = 0;  // カウンタをリセット
            }
        } else {
            notifyWarning();
        }
        check_counter++;
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

bool AntiTheftSystem::configureWiFi(const char* ip_address,
                                    const char* gateway_ip,
                                    const char* subnet_mask) {
    IPAddress local_ip;
    IPAddress gateway;
    IPAddress subnet;
    local_ip.fromString(ip_address);
    gateway.fromString(gateway_ip);
    subnet.fromString(subnet_mask);
    Serial.printf("Configuring WiFi with IP: %s, Gateway: %s, Subnet: %s\n",
                  local_ip.toString().c_str(), gateway.toString().c_str(),
                  subnet.toString().c_str());
    if (!WiFi.config(local_ip, gateway, subnet)) {
        M5.Display.fillScreen(RED);
        Serial.println("Failed to configure WiFi.");
        return false;
    }
    Serial.printf("WiFi configured with IP: %s, Gateway: %s, Subnet: %s\n",
                  local_ip.toString().c_str(), gateway.toString().c_str(),
                  subnet.toString().c_str());
    return true;
}

bool AntiTheftSystem::connectToWiFi(const char* ssid, const char* password) {
    Serial.printf("Connecting to WiFi >>> %s\n", ssid);
    if (WiFi.status() != WL_CONNECTED) {
        WiFi.begin(ssid, password);
        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
        }
        Serial.printf("Connected to WiFi >>> %s\n",
                      WiFi.localIP().toString().c_str());
    }
    return true;
}

void AntiTheftSystem::setDebugMode(bool enable) { debug = enable; }

void AntiTheftSystem::begin() {
    Serial.println("Anti-Theft System Starting...");
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi is not connected. Please connect to WiFi first.");
        M5.Display.fillScreen(RED);
        return;
    }
    WiFi.setAutoReconnect(true);
    xTaskCreatePinnedToCore(monitorTask, "Monitor", 8192, this, 1, nullptr,
                            APP_CPU_NUM);
    Serial.println("Anti-Theft System Started.");
}

void AntiTheftSystem::getCheckAPI() {
    Serial.printf("Sending GET request to %s\n", server_url);
    HTTPClient http;
    String url = String(server_url) + "/api/v1/check";
    http.begin(url);
    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.println(response);
    } else {
        Serial.printf("Error on HTTP request: %s\n",
                      http.errorToString(httpResponseCode).c_str());
    }
    http.end();
}