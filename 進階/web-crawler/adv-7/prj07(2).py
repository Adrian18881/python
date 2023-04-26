import requests
import os
import sys
from ttkbootstrap import *

os.chdir(sys.path[0])


def on_switch_change():
    global t
    if check_type.get() == True:
        t = (t - 32) * 5 / 9
        label3.config(text=f"溫度:{t}°C")
    else:
        t = t * (9 / 5) + 32
        label3.config(text=f"溫度:{t}°F")


def test():
    global t
    api_key = "0b901c6525e69d08f2619349785fadfb"  #API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry.get()
    units = "metric"
    lang = 'zh_tw'
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print(send_url)
    response = requests.get(send_url)
    info = response.json()
    if 'main' in info.keys():
        icon_code = info['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f'{icon_code}.png', "wb") as icon_file:
            icon_file.write(response.content)
        label3.config(text=f"溫度:{info['main']['temp']}°C")
        label4.config(text=f"描述:{info['weather'][0]['description']}")
        image = Image.open(f'{icon_code}.png')
        tK_image = ImageTk.PhotoImage(image)
        label2.config(image=tK_image)
        label2.image = tK_image
        t = info['main']['temp']
    else:
        print("city not found")


font_size = 20
window = tk.Tk()
window.title("my gui")
window.option_add("*font",
                  ("Helvetica", font_size))  #設定預設字型，這裡設為Helvetica, 大小是20
style = Style(theme="minty")  #設定主題
style.configure('my.TButton', font=('Helvetica', font_size))  # 設定按鈕字型
style.configure('my.TCheckbutton', font=('Helvetica', font_size))  # 設定按鈕字型
check_type = BooleanVar()
check_type.set(True)
check = Checkbutton(window,
                    text="溫度單位",
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    style='my.TCheckbutton')
check.grid(row=3, column=2)
entry = Entry(window, width=30)
entry.grid(row=0, column=2, padx=10, pady=10)
bttton = Button(window, text="獲得天氣資訊", command=test,
                style="my.TButton")  #設定按鈕樣式
bttton.grid(
    row=0,
    column=3,
)
label1 = Label(window, text="請輸入想搜尋的城市:")
label1.grid(
    row=0,
    column=1,
)
label2 = Label(window, text="天氣圖標")
label2.grid(
    row=1,
    column=1,
)
label3 = Label(window, text="溫度")
label3.grid(
    row=1,
    column=2,
)
label4 = Label(window, text="描述")
label4.grid(
    row=1,
    column=3,
)
window.mainloop()
