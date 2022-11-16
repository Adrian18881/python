import random

ans = random.randint(1, 100)
min = 0
max = 100
while True:
    x = int(input(f"請輸入{min}~{max}的整數:"))
    if x == ans:
        print("恭喜猜中!")
        break
    elif x < ans:
        print("再大一點")
        if min < x < max:
            min = x
    elif x > ans:
        print("再小一點")
        if min < x < max:
            max = x