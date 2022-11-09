import random as r

x = r.randint(1, 100)
while True:
    i = int(input("輸入0~100之間的數字:"))
    if i > x:
        print("再小一點")
    elif i < x:
        print("再大一點")
    elif i == x:
        print("答對了")
        break