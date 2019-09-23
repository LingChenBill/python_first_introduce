# Date:2019/9/22
# Author:Lingchen
# Mark:
#   多重循环
#   数据结构的推导式
#   列表的解析式
#   字典推导式: 创建字典必须满足键-值的两个条件才能达成
#   列表是有序的，可以使用Python中独有的函数enumerate来进行
import time

num_list = [6, 2, 7, 4, 1, 3, 5]
# sorted函数按照长短、大小、英文字母的顺序给每个列表中元素进行排序
print(sorted(num_list))
# 逆序排序
print(sorted(num_list, reverse=True))

num_list2 = [8, 9, 10]
for a, b in zip(num_list, num_list2):
    # print(b, 'is', a)
    print(a, 'is', b)

a = []
for i in range(1, 10):
    a.append(i)
print(a)

# 列表的解析式，执行效率比较高
b = [i for i in range(1, 10)]
print(b)

a = []
t0 = time.clock()

for i in range(1, 20000):
    a.append(i)
print(time.clock() - t0, 'seconds process time.')

t0 = time.clock()
b = [i for i in range(1, 20000)]
print(time.clock() - t0, 'seconds process time.')

a = [i ** 2 for i in range(1, 10)]
print(a)

c = [j + 1 for j in range(1, 10)]
print(c)

k = [n for n in range(1, 10) if n % 2 == 0]
print(k)

z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print(z)

d = {i: i + 1 for i in range(4)}
print(d)

g = {i: j for i, j in zip(range(1, 6), 'abcde')}
print(g)

g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
print(g)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(letters):
    print(letter, 'is', num + 1)

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
print(words)