from ttkbootstrap import *
import time


def start_progress():
    for i in range(101):
        progress['value'] = i
        percent_label.config(text=f"{i}%")
        window.update()
        time.sleep(0.05)


window = tk.Tk()
window.title("progress Bar Example")

progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=0, column=0)

percent_label = Label(window, text="")
percent_label.grid(row=0, column=1)

start_button = Button(window, text="start", command=start_progress)
start_button.grid(row=1, column=0, columnspan=2)

window.mainloop()