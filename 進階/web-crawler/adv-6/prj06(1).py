from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def on_switch_change():
    pass


window = tk.Tk()

check_type = BooleanVar()
check_type.set(True)

check_label = Label(window, text="True")
check_label.grid(row=1, column=2)

check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)

check.grid(row=1, column=1)
window.mainloop()  #讓視窗停留