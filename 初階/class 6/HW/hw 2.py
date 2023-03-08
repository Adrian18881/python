import turtle as t
import time
for i in range(1, 360, 6):
    t.forward(50)
    time.sleep(1)
    t.home()
    t.right(i)
    t.clear()
t.done()
