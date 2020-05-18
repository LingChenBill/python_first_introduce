# Date:2020/5/17
# Author:Lingchen
# Mark: 具名元组的属性和方法
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
# _fields属性是一个包含这个类所有字段名称的元组
print('City _fields: ', City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# _make()通过接受一个可迭代对象来生成这个类的一个实例
delhi = City._make(delhi_data)
print('delhi:', delhi)

# _asdict()把具名元组以collections.OrderedDict的形式返回，利用它来把元组里的信息友好地呈现出来
print('delhi_asdict: ', delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ': ', value)
