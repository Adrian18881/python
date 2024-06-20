#########################匯入模組#########################
import dht
import time
import mcu
import json
from machine import Pin, I2C, ADC
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "cringe", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("hello", on_message)
m = " no message"


i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
msg_json = {}
adc = ADC(0)
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7)
servo = mcu.servo(gpio.D8)


#########################主程式#########################
while True:
    light_value = adc.read()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    oled.fill(0)  # 清除螢幕
    oled.text(f"Humidity: {hum:02d}", 0, 0)
    oled.text(f"Temperature: {temp:02d}C", 0, 10)
    oled.text(f"Light: {light_value}", 0, 20)
    oled.show()

    msg_json["tempurature"] = temp
    msg_json["humidity"] = hum
    msg_json["lightsensor"] = light_value
    msg = json.dumps(msg_json)
    mqtt_client.publish("hello", msg)
    mqtt_client.check_msg()  # 等待已訂閱的主題發送資料

    if "ON" in m:
        LED.RED.value(1)
        LED.GREEN.value(1)
        LED.BLUE.value(1)
    elif "OFF" in m:
        LED.RED.value(0)
        LED.GREEN.value(0)
        LED.BLUE.value(0)

    if "open" in m:
        servo.write_angle(90)
    elif "close" in m:
        servo.write_angle(180)

    time.sleep(0.1)
