#########################匯入模組###############################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC, PWM, I2C
from time import sleep
import mcu
import ssd1306
#########################函式與類別定義#########################


def on_message(topic, msg):
    global m, t
    msg = msg.decode("utf-8") #Byte to str
    topic = topic.decode("utf-8")
    print(f"mt subscribe topic:{topic}, msg:{msg}")
    m = msg
    t = topic



#########################宣告與設定#############################
gpio = mcu.gpio()
i2c = I2C(scl = Pin(gpio.D1), sda = Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active = False, sta_active = True)
if wi.connect():
    print(f"IP = {wi.ip}")

MQTT = mcu.MQTT("cringe", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("cringe", on_message)

m=""
t=""
while True :
    MQTT.check_msg()
    oled.fill(0)
    oled.text(wi.ip, 0, 0)
    oled.text(t, 0, 10)
    oled.text(m, 0, 20)
    oled.show()
    time.sleep(0.1)





