# Date:2020/5/15
# Author:Lingchen
# Mark: Python内置的complex类可以用来表示二维向量
# Python有一个内置的函数叫repr，它能把一个对象用字符串的形式表达出来以便辨认

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        把一个对象用字符串的形式表达出来以便辨认
        %和str.format是两种格式化字符串的手段
        :return:
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """
        返回该向量的模
        :return:
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        如果一个向量的模是0，则返回False，否则返回True
        :return:
        """
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 测试Vector的特殊方法
v1 = Vector(2, 4)
v2 = Vector(2, 1)
# 隐式的调用__add__方法
print('v1 + v2: ', v1 + v2)

# 测试abs
v = Vector(3, 4)
print('v abs: ', abs(v))

# 测试向量的*法
print('v: ', v)
print('v * 3: ', v * 3)
print('v * 3 is abs: ', abs(v * 3))

# 测试向量的bool值
print('v bool: ', bool(v))

