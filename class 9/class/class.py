#for i in range(2, 10, 2):
#    print(i)
#else:
#    print("迴圈正常結束")

#i = 2
#while i < 6:
# print(i)
# i += 1
#else:
#    print("迴圈正常結束")

#i = 1
#while i < 6:
#    if i == 3:
#        break
#    print(i)
#    i += 1

#for i in range(1, 6):
#    if i == 3:
# break
#    print(i)

#for i in ra#nge(1, 6):
#    if i == 3:
#        continue
#    print(i)

#i = 1
#while i < 6:
#    if i == 3:
#        i += 1
#        continue
#    print(i)
#    i += 1
'''
while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")
    i = input("請輸入果汁編號")
    if i == '1':
        print("蘋果汁")
    elif i == '2':
        print("柳橙汁")
    elif i == '3':
        print("葡萄汁")
    elif i == '4':
        print("系統關閉，飲料自取")
        break
    else:
        print("重新輸入!")
'''
'''
import random

random.randrange(3)
random.randrange(0, 10, 2)


random.randint(1, 3)
random.randint(1, 10)
'''
'''
import random as a

print(a.random.randrange(3))
print(a.random.randrange(0,10,2))

print(a.random.randint(3))
print(a.random.randint(0,10,2))
'''

import random as r

x = r.randint(1, 100)
while True:
    i = int(input("輸入0~100之間的數字:"))
    if i > x:
        print("再小一點")

    elif i < x:
        print("再大一點")
    elif i == x:
        print("答對了")
        break
