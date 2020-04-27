# Date:2019/9/21
# Author:Lingchen
# Mark:
#   列表
#   使用列表的append方法可以向列表中添加新的元素
#   成员运算符与身份运算符
#   在Python中任何一个对象都要满足身份、类型、值这三个点，缺一不可
#   在Python中任何对象都可判断其布尔值，除了0、None和所有空的序列与集合的布尔值为False之外，其它的都为True

album = []
print("1:", album)

album = ['Blank Star', 'David Bowie', 25, True]
print("2:", album)

album.append('new song')
print("3:", album)

print("4:", album[0], album[-1])

print("5:", 'Blank Star' in album)

the_Eddie = 'Eddie'
name = 'Eddie'
print("6:",  the_Eddie == name)
print("7:", the_Eddie is name)

print("8:", bool(0))
print("9:", bool([]))
print("10:", bool(''))
print("11:", bool(False))
print("12:", bool(None))
