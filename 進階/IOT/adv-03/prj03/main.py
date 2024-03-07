#########################匯入模組#########################

from machine import Pin, ADC
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################

gpio = mcu.gpio()
light_sensor = ADC(0)  #建立ADC物件

#########################主程式#########################

while True:
    light_sensor_reading = light_sensor.read() #讀取此類比數位轉換器輸出
    print(f"value = {light_sensor_reading}, {round(light_sensor_reading *100/1024)}%")
    sleep(1) #延遲一秒