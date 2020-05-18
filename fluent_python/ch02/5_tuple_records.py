# Date:2020/5/16
# Author:Lingchen
# Mark: 元组其实是对数据的记录
#       元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置，正是这个位置信息给数据赋予了意义
#       元组拆包可以应用到任何可迭代对象上，唯一的硬性要求是，被可迭代对象中的元素数量必须要跟接受这些元素的元组的空档数一致
#       在元组拆包中使用 * 也可以帮助我们把注意力集中在元组的部分元素上
import os
from collections import namedtuple

lax_coordinates = (33.9425, -118.408056)
print('lax_coordinates: ', lax_coordinates)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print(city, year, pop, chg, area)

# %格式运算符能被匹配到对应的元组元素上
print('passport: ')
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 拆包（unpacking）,因为元组中第二个元素对我们没有什么用，所以它赋值给"_"占位符
print('country: ')
for country, _ in traveler_ids:
    print(country)

# 元组拆包
latitude, longitude = lax_coordinates
print('latitude', latitude)
print('longitude', longitude)

# * 运算符把一个可迭代对象拆开作为函数的参数
divmod(20, 8)
print('divmod: ', divmod(20, 8))

t = (20, 8)
print('divmod *: ', divmod(*t))
quotient, remainder = divmod(*t)
# print('%s/%s' % (quotient, remainder))
print((quotient, remainder))

_, filename = os.path.split('/home/lucciy/.ssh/idrsa.pub')
print('filename: ', filename)

# 函数用 *args来获取不确定数量的参数算是一种经典写法了
a, b, *rest = range(5)
print('a, b, rest: ', a, b, rest)

a, b, *rest = range(3)
print('a, b, rest two: ', a, b, rest)

a, b, *rest = range(2)
print('a, b, rest: ', a, b, rest)

# * 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
a, *body, c, d = range(5)
print('a, *body, c, d: ', a, body, c, d)
*head, b, c, d = range(5)
print('*head, b, c, d: ', head, b, c, d)

# 用嵌套元组来获取经度
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15}|{:9}|{:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15}|{:9.4f}|{:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# 定义和使用具名元组
# 创建一个具名元组需要两个参数：一个是类名，一个是类的各个字段的名字
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print('tokyo: ', tokyo)
print('tokyo.population: ', tokyo.population)
print('tokyo.coordinates: ', tokyo.coordinates)
print('tokyo[1]: ', tokyo[1])

print('City._fields: ', City._fields)

