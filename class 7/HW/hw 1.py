x = int(input("輸入箭頭大小"))
for i in range(1, x + 1):
    print(" " * (x - i) + "*" * (i * 2 - 1))
for i in range(x):
    print(" " * (x - 1) + "*")
