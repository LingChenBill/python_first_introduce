# Date:2020/5/16
# Author:Lingchen
# Mark: 列表推导的作用只有一个：生成列表
#       可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择
#       生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已
#       用到生成器表达式之后，内存里不会留下一个生成的组合的列表，避免额外的内存占用
import array

symbols = '$¢£¥€¤'
print('tuple: ', tuple(ord(symbol) for symbol in symbols))

print('array.array: ', array.array('I', (ord(symbol) for symbol in symbols)))

# 使用生成器表达式计算笛卡儿积
print('builder tshirt: ')
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

