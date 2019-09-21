# Date:2019/9/21
# Author:Lingchen
# Mark:
#   列表
#   使用列表的append方法可以向列表中添加新的元素
#   成员运算符与身份运算符
#   在Python中任何一个对象都要满足身份、类型、值这三个点，缺一不可
#   在Python中任何对象都可判断其布尔值，除了0、None和所有空的序列与集合的布尔值为False之外，其它的都为True

album = []
print(album)

album = ['Blank Star', 'David Bowie', 25, True]
print(album)

album.append('new song')
print(album)

print(album[0], album[-1])

print('Blank Star' in album)

the_Eddie = 'Eddie'
name = 'Eddie'
print(the_Eddie == name)
print(the_Eddie is name)

print(bool(0))
print(bool([]))
print(bool(''))
print(bool(False))
print(bool(None))
