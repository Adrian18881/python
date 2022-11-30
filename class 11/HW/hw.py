bag2 = []
for i in bag:
    if not (i in bag2):
        bag2.append(i)
        print(f'{i}={bag.count(i)}')