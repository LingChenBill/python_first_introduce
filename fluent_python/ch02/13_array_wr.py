# Date:2020/5/19
# Author:Lingchen
# Mark: 一个浮点型数组的创建、存入文件和从文件读取的过程
from array import array
from random import random

# 利用一个可迭代对象来建立一个双精度浮点数组（类型码为'd'）,生成器表达式
floats = array('d', (random() for i in range(10**7)))
print('floats[-1]: ', floats[-1])

fp = open('floats.bin', 'wb')
# 把数组存入一个二进制文件里
floats.tofile(fp)
fp.close()

# 新建一个双精度浮点空数组
floats2 = array('d')
fp = open('floats.bin', 'rb')
# 把1000万个浮点数从二进制文件里读取出来
floats2.fromfile(fp, 10**7)
fp.close()
print('floats2[-1]: ', floats2[-1])

print(floats2 == floats)
