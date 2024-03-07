#########################匯入模組#########################

from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################

#########################宣告與設定#########################

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式#########################



while True:
    for n in range(1023, 0, -1):
        led.duty(n)
        sleep(0.002)

    for n in range(0, 1023, 1):
        led.duty(n)
        sleep(0.002)


