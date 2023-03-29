from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def show_result():
    entry_text = entry.get()
    x = eval(entry_text)
    lable.config(text=x)


font_size = 20
window = tk.Tk()
window.title("My GUI")
window.option_add("*font", ("Helvetica", font_size))
style = Style(theme="minty")
style.configure("my.TButton", font=("Helvetica", font_size))

button2 = Button(window,
                 text="顯示計算結果",
                 command=show_result,
                 style="my.TButton")
button2.grid(row=1, column=0, columnspan=2, sticky="N")
entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="E")

lable = Label(window, text="計算結果")
lable.grid(row=2, column=0, columnspan=2, sticky="N")

window.mainloop()
