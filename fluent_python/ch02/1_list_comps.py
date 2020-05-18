# Date:2020/5/16
# Author:Lingchen
# Mark: 列表推导（list comprehension）简称为listcomps
#       把一个字符串变成Unicode码位的列表
#       Python3中都有了自己的局部作用域，表达式内部的变量和赋值只在局部起作用
#       表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响它们

symbols = '$1a#A%Z^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print('codes: ', codes)

codes_oth = [ord(symbol) for symbol in symbols]
print('codes_oth:', codes_oth)

# Python3中都有了自己的局部作用域
x = 'my precious'
dummy = [x for x in 'ABC']
print('x: ', x)
print('dummy: ', dummy)

# x的值被保留了
# 列表推导也创建了正确的列表
x = 'ABC'
dummy = [ord(x) for x in x]
print('x other:', x)
print('dummy other: ', dummy)

# 用列表推导和map/filter组合来创建同样的表单
beyond_ascii = [ord(s) for s in symbols if ord(s) > 90]
print('beyond_ascii: ', beyond_ascii)
print('map: ', map(ord, symbols))
beyond_ascii = list(filter(lambda c: c > 90, map(ord, symbols)))
print('beyond_ascii filter: ', beyond_ascii)
