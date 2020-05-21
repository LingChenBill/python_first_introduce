# Date:2020/5/20
# Author:Lingchen
# Mark: 对numpy.ndarray的行和列进行基本操作
import numpy

a = numpy.arange(12)
print('a: ', a)
print('type a: ', type(a))

# 数组的维度，它是一个一维的，有12个元素的数组
print('a.shape: ', a.shape)

a.shape = 3, 4
print('a shaped: ', a)

print('a[2]: ', a[2])
print('a[:, 1]: ', a[:, 1])

print('a.transpose: ', a.transpose())

