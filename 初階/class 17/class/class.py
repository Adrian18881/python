import datetime

print(datetime.date.today())
x = datetime.date.today()
day = input("What is your birthday?")
print(day)
birth = datetime.datetime.strptime(day, "%Y/%m/%d")
print(birth.date() - x)