import turtle as t


def l(f, j):
    f = input("請輸入x座標")
    j = input("請輸入y座標")
    t.penup()


for i in range(f, j):
    t.forward(i)
    t.stamp()
t.done()
