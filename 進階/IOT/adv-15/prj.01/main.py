#########################匯入模組#########################

import paho.mqtt.client as mqtt
import time
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

#########################函式與類別定義#########################


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


#########################宣告與設定#########################

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.0)

#########################主程式#########################

while True:
    ans = input("請輸入想跟AI說的話:")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
                    你是一個控制室內燈光開關和車庫的AI
                    你可以根據使用者說的話來判斷是否要開燈或關燈或開車庫門或關車庫門
                    不要回答其他的字串
                    你只能回答'on'或'off'或'None'或'open'或'close'
                    你可以同時決定多個裝置的狀態
                    'on'代表開燈
                    'off'代表關燈
                    'open'代表開車庫門
                    'close'代表關車庫門
                    'None'代表不動作
                    不能回答其他的字串
                    """
            ),
            HumanMessage(content=ans),
        ]
    )
    print(msg.content)

    result = client.publish("cringe", msg.content)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成
    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
