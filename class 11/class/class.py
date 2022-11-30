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

# l = ['a', 'b', 'c', 'a']
# index = l.index('a')
# print(index)

bag = []
size = int(input("請輸入背包大小:"))
for i in range(size):
    t = input("請輸入想裝的東西:")
    bag.append(t)
    print(bag)

# r = input("請輸入想拿出來的東東:")
# while r in bag:

#     bag.remove(r)

# print(bag)

bag2 = []
for i in bag:
    if not (i in bag2):
        bag2.append(i)
        print(f'{i}={bag.count(i)}')
# c = (input("請輸入想計算數量的東東:"))
# print(bag.count(c))