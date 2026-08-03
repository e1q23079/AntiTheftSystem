#include <HTTPClient.h>
#include <M5unified.h>
#include <WiFi.h>

#pragma once

/*
 * @brief M5Stackデバイスの盗難防止システムを管理するクラスです。
 */
class AntiTheftSystem {
   public:
    /*
     * @brief コンストラクタ。サーバーURLを設定します。
     * @param server_url 盗難防止システムのサーバーURL
     */
    AntiTheftSystem(const char* server_url);

    /*
     * @brief WiFiの設定を行います。
     * @param ip_address デバイスのIPアドレス
     * @param gateway_ip ゲートウェイのIPアドレス
     * @param subnet_mask サブネットマスク
     */
    bool configureWiFi(const char* ip_address, const char* gateway_ip,
                       const char* subnet_mask);
    /*
     * @brief WiFiに接続します。
     * @param ssid WiFiのSSID
     * @param password WiFiのパスワード
     * @return 接続が成功した場合はtrue、失敗した場合はfalseを返します。
     */
    bool connectToWiFi(const char* ssid, const char* password);

    /*
     * @brief デバッグモードを設定します。
     * @param enable デバッグモードの有効化フラグ
     */
    void setDebugMode(bool enable);
    /*
     * @brief
     * 盗難防止システムを開始します。WiFi接続が確立されている場合、デバイスの監視を開始します。
     */
    void begin();

   private:
    /*
     * @brief デバイスの監視タスクを実行します。
     * @param arg タスクに渡す引数（AntiTheftSystemのインスタンスへのポインタ）
     */
    static void monitorTask(void* arg);
    /*
     * @brief
     * デバイスの監視を行います。WiFi接続が切断された場合、警告を通知します。
     */
    void monitorDevices();
    /*
     * @brief サーバーのチェックAPIにアクセスします。
     */
    void getCheckAPI();
    /**
     * @brief 警告を通知します。
     */
    void notifyWarning();

    const char* server_url;  // 盗難防止システムのサーバーURL

    int check_counter = 0;  // サーバーへのアクセスカウンタ

    bool debug = false;  // デバッグモードの有効化フラグ
};