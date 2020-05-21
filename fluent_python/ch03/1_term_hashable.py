# Date:2020/5/21
# Author:Lingchen
# Mark: 原子不可变数据类型（str、bytes和数值类型）都是可散列类型
#       Python里所有的不可变类型都是可散列的。这个说法是不准确的
#       比如：虽然元组本身是不可变序列，它里面的元素可能是其他可变类型的引用

tt = (1, 2, (30, 40))
print('hash(tt): ', hash(tt))

t1 = (1, 2, [30, 40])
# print('hash(t1): ', hash(t1))

tf = (1, 2, frozenset([30, 40]))
print('hash(tf): ', hash(tf))

a = dict(one=1, two=2, three=3)
print('a: ', a)
b = {'one': 1, 'two': 2, 'three': 3}
print('b: ', b)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print('c: ', c)
d = dict([('two', 2), ('one', 1), ('three', 3)])
print('d: ', d)
e = dict({'three': 3, 'one': 1, 'two': 2})
print('e: ', e)

print('a==b==c==d==e: ', a == b == c == d == e)


