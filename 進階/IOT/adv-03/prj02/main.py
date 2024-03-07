#########################匯入模組#########################

from machine import Pin, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5, Pin.OUT), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6, Pin.OUT), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7, Pin.OUT), freq=frequency, duty=duty_cycle)


#########################主程式#########################

while True:
    for duty_cycle in range(1023, 0, -1):
        RED.duty(duty_cycle)
        GREEN.duty(1023 - duty_cycle)
        sleep(0.002)

    for duty_cycle in range(1023, 0, -1):
            GREEN.duty(duty_cycle)
            BLUE.duty(1023 - duty_cycle)
            sleep(0.002)

    for duty_cycle in range(1023, 0, -1):
            BLUE.duty(duty_cycle)
            RED.duty(1023 - duty_cycle)
            sleep(0.002)




