h = float(input("請輸入身高"))
w = float(input("請輸入體重"))
bmi = w / h**2
print("你的BMI為" + str(bmi))
if bmi >= 14.8 and bmi <= 20.7:
    print("bmi值正常")
elif bmi >= 20.7:
    print("bmi值重")
elif bmi <= 14.8:
    print("bmi值輕")
