n = int(input("開始植樹"))
y = int(input("結束植樹"))
for x in range(n, y):
    i = 2
    while x % i != 0 and i != x:
        i += 1

    if i == x:
        print(x)
