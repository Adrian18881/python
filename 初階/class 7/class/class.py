'''
import turtle as t

t.tracer(0, 0)
t.fillcolor("yellow")
t.begin_fill()

for i in range(1, 6):
    t.pensize(5)
    t.pencolor("yellow")
    t.forward(200)
    t.left(144)

t.end_fill()
t.done()
'''
x = int(input("請輸入一個數字:"))
s = 0
for i in range(1, x + 1):
    s = s + i
print(s)
