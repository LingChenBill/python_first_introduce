# Date:2019/10/4
# Author:Lingchen
# Mark:
#   lambda表达式的学习
#   返回两个参数的和: a + b
#   Lambda函数可以在需要函数对象的任何地方使用。它们在语法上限于单个表达式。
#   从语义上来说，它们只是正常函数定义的语法糖
#   1.使用一个lambda表达式来返回一个函数
#   2.传递一个小函数作为参数


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
