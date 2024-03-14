#########################匯入模組#########################
import network

#########################函式與類別定義#########################

#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF) #初始化 STA 模式
ap = network.WLAN(network.AP_IF) #初始化 AP 模式
ap.active(False) #關閉 AP 模式
wlan.active(True) #開啟 STA 模式

#搜尋 WIFI
wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])

#選擇要連接的WIFI
wlSSID = "SingularClass"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD) 
while not(wlan.isconnected()): #等待連接成功
    pass
print("connect successfully", wlan.ifconfig()) #顯示連接成功的 IP
#########################主程式#########################