try:
    f = float(input("請輸入華氏溫度:"))
except:
    print('發生錯誤')
else:
    c = 5 / 9 * (f - 32)
    print("華氏溫度" + str(f) + "F等於攝氏溫度" + str(c) + "C")
