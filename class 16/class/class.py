# import random as r

# def roll_dice(x):
#     l = []
#     for i in range(x):
#         l.append(r.randint(1, 6))
#     return l


# n = int(input("請輸入擲骰子的次數:"))
# n1 = roll_dice(n)
# print(n1)
# print(f"加總={sum(n1)}")
def exit(b):
    print(f"平均是{sum(b.values())/len(b)}")


def add(b):
    key = input("請輸入科目:")
    value = int(input("請輸入成績:"))
    b[key] = value


def delete(b):
    r = input("請輸入想刪除的key:")
    b.pop(r, "")
    print(b)


b = {}
while True:
    for key, value in b.items():
        print(key + ":", value)
    print("1. 新增成績")
    print("2. 刪除成績")
    print("3. 離開系統")
    ans = input("請輸入功能選項:")
    if ans == "1":
        add(b)
    elif ans == "2":
        delete(b)
    elif ans == "3":
        exit(b)
        break