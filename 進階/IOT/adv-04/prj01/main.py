#########################匯入模組#########################

from machine import Pin, ADC, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################

gpio = mcu.gpio()
light_sensor = ADC(0)  #建立ADC物件

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5, Pin.OUT), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6, Pin.OUT), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7, Pin.OUT), freq=frequency, duty=duty_cycle)

#########################主程式#########################

while True:
    light_sensor_reading = light_sensor.read() #讀取此類比數位轉換器輸出
    print(f"value = {light_sensor_reading}, {round(light_sensor_reading *100/1024)}%")

    if light_sensor_reading > 700:
        GREEN.duty(light_sensor_reading)
    else:
        GREEN.duty(0)
