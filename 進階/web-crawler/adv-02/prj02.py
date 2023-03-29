from tkinter import *
from PIL import Image, ImageTk
import sys
import os

os.chdir(sys.path[0])


def exit_fun():
    windows.destroy()


def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "d":
        canvas.move(rect, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)


windows = Tk()  #召喚視窗
windows.title("My first GUI")  #取個名字
quit_btn = Button(windows, text="齊齊回家遊戲", command=exit_fun)
quit_btn.pack()
canvas = Canvas(windows, width=400, height=600)
canvas.pack()
windows.iconbitmap("crocodile2.ico")
# img = PhotoImage(file="crocodile2.gif")
image = Image.open("0005404101_B.jpg")
img = ImageTk.PhotoImage(image)
my_img = canvas.create_image(300, 300, image=img)
circle = canvas.create_oval(250, 150, 300, 200, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300,
                         100,
                         text="幹你娘",
                         fill="black",
                         font=('Arial', 30))
canvas.bind_all('<Key>', move_circle)
windows.mainloop()