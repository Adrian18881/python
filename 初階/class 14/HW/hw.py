b = {}
while True:
    for key, value in b.items():
        print(key + ":", value)
    print("1. 新增成績")
    print("2. 刪除成績")
    print("3. 離開系統")
    ans = input("請輸入功能選項:")
    if ans == "1":
        key = input("請輸入科目:")
        value = int(input("請輸入成績:"))
        b[key] = value
    elif ans == "2":
        r = input("請輸入想刪除的key:")
        b.pop(r, "")
        print(b)
    elif ans == "3":
        print(f"平均是{sum(b.values())/len(b)}")
        break