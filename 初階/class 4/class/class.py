'''
name = 'Python'
age = 31
new_str = "我是" + name + "," + "今年" + str(age) + "歲了"
new_str_1 = "我是%s,今年%d歲了" % (name, age)
new_str_2 = "我是{},今年{}歲了".format(name, age)
new_str_3 = "我是{a},今年{b}歲了".format(b=age, a=name)
new_str_4 = f"我是{name},今年{age}歲了"
print(new_str)
print(new_str_1)
print(new_str_2)
print(new_str_3)
print(new_str_4)
'''
'''
try:
    num = int(input('請輸入一個數字'))
    total = num + 1
    print(total)
except ValueError:
    print('請輸入數字')
except:
    print('發生錯誤')
else:
    print('成功執行')
finally:
    print('程式結束')
'''