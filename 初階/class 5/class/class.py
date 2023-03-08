# password = input("請輸入成績")
# if password == "1234":
#     print("hello grandmother")
# elif password == "":
#     print("hello grandfather")
# elif password == "123456":
#     print("hello Adrian")
# elif password == "1234567":
#     print("hello mom")
# elif password == "12345678":
#     print("hello dad")
# elif password == "123456789":
#     print("hello sister")
# else:
#     print("請重新輸入")

s = int(input("請輸入成績："))
if s >= 90:
    print("A")
elif s >= 80 and s <= 89:
    print("B")
elif s >= 70 and s <= 79:
    print("C")
elif s >= 60 and s <= 69:
    print("D")
elif s <= 59:
    print("E")