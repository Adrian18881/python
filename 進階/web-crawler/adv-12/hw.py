import requests
import os
import sys
from ttkbootstrap import *

font_size = 20
window = tk.Tk()
window.title("Weather App")
window.option_add("*font", ("Helvetica", font_size))
style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))
icon_label = Label(window, text="請輸入youtube網址")
icon_label.grid(row=0, column=0)
lon_entry = Entry(
    window,
    width=20,
)
lon_entry.grid(
    row=0,
    column=1,
)
search_button = Button(window, text="獲得天氣資訊", style='my.TButton')
search_button.grid(
    row=0,
    column=2,
)
search_button = Button(window, text="下載影片", style='my.TButton')
search_button.grid(
    row=1,
    column=2,
)
icon_label = Label(window, text="選擇影片解析度")
icon_label.grid(row=1, column=0)
icon_label = Label(window, text="")
icon_label.grid(row=2, column=0)
window.mainloop()
