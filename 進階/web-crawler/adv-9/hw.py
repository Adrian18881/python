import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
import os
import sys
import requests
import datetime
from PIL import Image, ImageTk

os.chdir(sys.path[0])  # 設定工作目錄


def get_weather_info():
    global units
    city_name = city_name_entry.get()
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)  # 發送請求，獲得天氣資訊
    info = response.json()  # 將json格式轉換為字典

    if "main" in info.keys():  # 如果有main這個key，代表有天氣資訊
        global current_temperature
        current_temperature = info["main"]["temp"]
        weather_description = info["weather"][0]["description"]
        icon_code = info["weather"][0]["icon"]

        # 下載並保存天氣圖標
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        # 更新GUI
        image = Image.open(f"{icon_code}.png")  # 打開圖片
        tk_image = ImageTk.PhotoImage(image)  # 將圖片轉換為tkinter可以使用的格式
        icon_label.config(image=tk_image)  # type: ignore # 更新圖片
        icon_label.image = tk_image  # type: ignore # 避免被記憶體回收機制回收圖片

        temperature_label.config(text=f"溫度: {current_temperature}°C")
        description_label.config(text=f"描述: {weather_description}")

    else:  # 如果沒有main這個key，代表沒有天氣資訊
        description_label.config(text=f"描述: City Not Found")


def on_switch_change():
    global units, current_temperature
    if check_type.get():
        units = "metric"

    else:
        units = "imperial"

    if temperature_label.cget("text") != "溫度: ?°C":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°C")
        elif units == "imperial":
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°F")


api_key = "892da2f13edf3c7f382637760e72d224"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
lang = "zh_tw"

font_size = 20
window = tk.Tk()
window.title("Weather App")
window.option_add("*font", ("Helvetica", font_size))

style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))

# 城市名稱輸入框
city_name_label = Label(window, text="請輸入想搜尋的城市:")
city_name_label.grid(row=0, column=0)
city_name_entry = Entry(window)
city_name_entry.grid(row=0, column=1)

# 查詢按鈕
search_button = Button(window,
                       text="獲得天氣資訊",
                       command=get_weather_info,
                       style='my.TButton')
search_button.grid(row=0, column=2)

# 天氣圖標
icon_label = Label(window, text="天氣圖標")
icon_label.grid(row=1, column=0)

# 溫度標籤
temperature_label = Label(window, text="溫度: ?°C")
temperature_label.grid(row=1, column=1)

# 描述標籤
description_label = Label(window, text="描述: ?")
description_label.grid(row=1, column=2)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    text="溫度單位(°C/°F)",
                    style='my.TCheckbutton')
check.grid(row=2, column=1)


def on_closing():
    window.destroy()
    plt.close('all')


def on_closing():
    window.destroy()
    plt.close('all')


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")

draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)

# 運行應用程式
window.mainloop()