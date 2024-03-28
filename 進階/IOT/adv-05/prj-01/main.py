#########################匯入模組#########################

import mcu

#########################函式與類別定義#########################

wi = mcu.wifi("SingularClass", "Singular#1234")
#wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)

#搜尋WIFI
wi.scan()

#選擇要連接的wifi
#if wi.connect("SingularClass", "Singular#1234")
if wi.connect():
    print(f"IP={wi.ip}")

#########################宣告與設定#########################

#########################主程式#########################