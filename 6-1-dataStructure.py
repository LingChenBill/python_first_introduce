# Date:2019/9/22
# Author:Lingchen
# Mark:
#   内置数据结构
#   Python有四种数据结构: 列表、字典、元组、集合
#   列表: 列表中的每一个元素都是可变的
#        列表中的元素是有序的，也就是说每一个元素都有一个位置
#        列表可以容纳Python中的任何对象
#   列表数据的增删改查

list = ['val1', 'val2', 'val3', 'val4']
dict = {'key1': 'val1', 'key2': 'val2'}
tuple = ('val1', 'val2', 'val3', 'val4')
set = {'val1', 'val2', 'val3', 'val4'}

print(list)
print(dict)
print(tuple)
print(set)

Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(Weekday[0])
print(Weekday[-1])

all_in_list = [
    1,
    1.0,
    'a word',
    print(1),
    True,
    [1, 2],
    (1, 2),
    {'key': 'value'}
]
print(all_in_list)

fruit = ['pineapple', 'pear']
# insert方法，必须指定在列表中要插入的新的元素的位置，插入元素的实际位置是在指定位置元素之前的位置
fruit.insert(1, 'grape')
print(fruit)

fruit[0:0] = ['orange']
print(fruit)

# 删除元素
fruit.remove('grape')
print(fruit)

fruit[0] = 'Grapefruit'
print(fruit)

# 删除还可以使用del关键字来声明
del fruit[0:2]
print(fruit)

# 列表的索引和字符串是一样的
periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])
