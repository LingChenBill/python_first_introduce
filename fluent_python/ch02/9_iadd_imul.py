# Date:2020/5/17
# Author:Lingchen
# Mark: 增量赋值运算符 += 和 *= , 就地加法（乘法）

# # 对可变元组上操作
# l = [1, 2, 3]
# print('l: ', l)
# print('id(l): ', id(l))
#
# l *= 2
# print('l *= 2 : ', l)
# print('id(l): ', id(l))
#
# # 对不可变元组上操作，新建对象，效率低
# t = (1, 2, 3)
# print('t: ', t)
# print('id(t): ', id(t))
# t *= 2
# print('t *= 2 : ', t)
# print('id(t): ', id(t))

# 不要把可变对象放在元组里面
# 增量赋值不是一个原子操作
# TypeError: 'tuple' object does not support item assignment
t = (1, 2, [30, 40])
t[2] += [50, 60]
print('t += : ', t)
