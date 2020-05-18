# Date:2020/5/18
# Author:Lingchen
# Mark: list.sort方法和内置函数sorted

fruits = ['grape', 'raspberry', 'apple', 'banana']
print('fruits: ', fruits)

print('sorted(fruits): ', sorted(fruits))
print('sorted reverse: ', sorted(fruits, reverse=True))
print('sorted len: ', sorted(fruits, key=len))
print('sorted len reverse: ', sorted(fruits, key=len, reverse=True))
print('fruits 2: ', fruits)
# 对原序列就地排序，返回值None会被控制台忽略
fruits.sort()
print('fruits sort(): ', fruits)



