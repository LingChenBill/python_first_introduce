# Date:2020/5/17
# Author:Lingchen
# Mark: 在切片和区间操作里不包含区间范围的最后一个元素是Python的风格，以0为起始下标的传统

l = [10, 20, 30, 40, 50, 60]
print('l[:2]: ', l[:2])
print('l[2:]: ', l[2:])
print('l[:3]: ', l[:3])
print('l[3:]: ', l[3:])

# s[a:b:c]的形式对s在a和b之间以c为间隔取值。c的值还可以为负,负值意味着反向取值
s = 'bicycle'
print('s[::3]: ', s[::3])
print('s[::-1]: ', s[::-1])
print('s[::2]: ', s[::2])
print('s[::-2]: ', s[::-2])

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[1:]
print('line_items: ', line_items)

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# 给切片赋值
l = list(range(10))
print('l: ', l)
print('l[2:5]: ', l[2:5])
l[2:5] = [20, 30]
print('l1: ', l)
# l[2:5] = [20, 30, 40]
# print('l2: ', l)

del l[5:7]
print('l3: ', l)

l[3::2] = [11, 22]
print('l3: ', l)

# 如果赋值的对象是一个切片，那么赋值语句的右边必须是个可迭代对象
# 即便只有单独一个值，也要把它转换成可迭代的序列
l[2:5] = [100]
print('l4: ', l)


