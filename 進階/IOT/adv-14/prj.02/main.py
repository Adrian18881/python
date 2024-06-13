import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.0)

from langchain_core.messages import HumanMessage

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
