'''
password = ''
while password != "1234":
    password = input("請輸入密碼")
    if password == "1234":
        print("hello dude")
    else:
        print("滾回去重新輸入!!!")
'''
x = int(input("輸入一個數字"))
i = 2
while x % i != 0 and i != x:
    i += 1
if i == x:
    print("yes")
else:
    print("nope")
