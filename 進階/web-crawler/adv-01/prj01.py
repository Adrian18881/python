from tkinter import *


def hi_fun():
    global change
    print("hi  dude")  #按下按鈕要執行的程式
    if change == False:
        display.config(text="hi buddy", fg="red", bg="black")
    else:
        display.config(text="hi buddy", fg="black", bg="red")
    change = not (change)


change = False

win = Tk()  #召喚視窗
win.title("My first GUI")  #取個名字

btn = Button(win, text="Click me", command=hi_fun, fg="grey", bg="#FFD300")
#按鈕物件    #執行視窗  #按鈕上文字         #待執行程式

btn.pack()

#標籤物件       #執行視窗    #標籤名字  #字體顏色    #背景顏色
display = Label(win, text="hi", fg="red", bg="black")
display.pack()

win.mainloop()  #讓視窗停留
