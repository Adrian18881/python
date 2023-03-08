# ['蘋果', '香蕉', '葡萄']

# []
# ['蘋果']
# ['a', 'b']
# [1, 2, 3]

# [1, 2] + ['b', 'c']

# [1, 2] * 2

# l = ['a', 'b', 'c']
# l[0]
# l[1]
# l[2]

# l = [0, 1, 2, 3, 4]
# l[0:3]
# l[3:5]

#len=取長度
# len([])
# len(['蘋果'])
# len(['a', 'b'])
# len([1, 2, 3])

# l = ['a', 'b', 'c']
# for index in range(len(l)):
#     print(l[index])

# l = ['a', 'b', 'c']
# for element in l:
#     print(element)

# max([])
# max(['蘋果', '香蕉', '橘子'])
# max(['a', 'b'])
# max([1, 2, 3])

# min([])
# min(['蘋果', '香蕉', '橘子'])
# min(['a', 'b'])
# min([1, 2, 3])

# list('abc')
# list([4, 5, 6])
# list(range(3))
# '1,2,3'.split(',')
# '2020/1/1'.split('/')

# img = ['1', '2', '3']
# '-'.join(img)

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)
# 4:38
# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'A')
# print(l)

# l = [1, 2, 3]
# l.pop()
# print(l)

# l = [1, 2, 3]
# l.pop(0)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort()
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l)

# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l)

juice = ['蘋果汁', '柳橙汁', '葡萄汁', '粑粑', '系統關閉']

while True:
    for index in range(len(juice)):
        print(f'{index+1}.{juice[index]}')
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(juice):
            print("輸入錯誤查無此果汁，請重新輸入編號")
        elif ans == len(juice):
            print("~~~系統已炸，滾吧!!ㄚㄚㄚㄚ ~~~")
            break
        else:
            print(f"~~~~~您的商點是{juice[ans-1]}歐~~~~~")
