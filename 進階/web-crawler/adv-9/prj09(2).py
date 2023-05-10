import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
import os
import sys
import requests
import datetime

os.chdir(sys.path[0])


def draw_graph():
    api_key = "892da2f13edf3c7f382637760e72d224"

    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    lon = "121.5319"
    lat = "25.0478"
    exclude = "minutely,hourly"
    units = "metric"
    lang = "zh_tw"

    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    print(send_url)

    response = requests.get(send_url)
    info = response.json()

    X_date = []
    Y_temp = []
    if "daily" in info.keys():
        for i in range(7):
            temp = info["daily"][i]["temp"]["day"]
            time = datetime.datetime.fromtimestamp(
                info["daily"][i]["dt"]).strftime("%m/%d")
            print(f"{time}的溫度是{temp}度")
            X_date.append(time)
            Y_temp.append(temp)

    else:
        print("Request Fail")
    font = FontProperties(fname='NotoSansTC-Black.otf', size=14)

    fig, ax = plt.subplots()
    ax.plot(X_date, Y_temp)
    ax.set_xlabel("7天天氣預測", fontproperties=font)
    ax.set_ylabel("溫度(°C)", fontproperties=font)
    ax.set_title("日期", fontproperties=font)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas = canvas.get_tk_widget()
    canvas.grid(row=0, column=0, padx=10, pady=10)


def on_closing():
    window.destroy()
    plt.close('all')


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")

draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()