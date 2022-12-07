bag = []
bag2 = []
end = True
while end == True:
    print(f'目前已點的餐{bag}')
    print('1.新增餐點')
    print('2.移除餐點')
    print('3.提交餐點')

    try:
        aa = int(input('請輸入功能選項:'))
    except:
        print('請輸入正確數字')
    else:
        # aa = int(input('請輸入功能選項:'))
        if aa == 1:
            print('1. 蘋果汁')
            print('2. 柳橙汁')
            print('3. 葡萄汁')
            try:
                aaa = int(input('請輸入餐點編號:'))
            except:
                print('請輸入正確數字')
            else:
                if aaa == 1:
                    bag.append('蘋果汁')
                elif aaa == 2:
                    bag.append('柳橙汁')
                elif aaa == 3:
                    bag.append('葡萄汁')

        if aa == 2:
            bbb = input('請輸入想移除的餐點完整名稱:')
            if bbb == '蘋果汁':
                while '蘋果汁' in bag:
                    bag.remove('蘋果汁')
                    print('移除完成')
            if bbb == '柳橙汁':
                while '柳橙汁' in bag:
                    bag.remove('柳橙汁')
                    print('移除完成')
            if bbb == '葡萄汁':
                while '葡萄汁' in bag:
                    bag.remove('葡萄汁')
                    print('移除完成')
            else:
                print('請輸入完整名稱')
        if aa == 3:
            print('您點的餐點為')
            for i in bag:
                if not (i in bag2):
                    bag2.append(i)
                    print(f'{i}={bag.count(i)}')
                    end = False
        else:
            print('請輸入正確數字')

print('菜單已提交囉!')
