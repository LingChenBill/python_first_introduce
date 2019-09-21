# Date:2019/9/21
# Author:Lingchen
# Mark:
#   Define a function named 'function' which has two arguments: arg1 and arg2, returns the result--'somethings'
#   摄氏度转化公式: F = 9/5 * C + 32
#   位置参数传值方式
#   关键词参数传值方式

import numpy


def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    # print(str(fahrenheit) + 'F')
    return str(fahrenheit) + 'F'


C2F = fahrenheit_converter(35)
print(C2F)


# 重量转换函数
def weight_converter(g):
    return str(g/1000) + 'KG'


g2KG = weight_converter(1000)
print(g2KG)


# 直角三角形斜边长的函数
def triangle_third_side(side1, side2):
    third_side = (side1 * side1 + side2 * side2) ** 0.5
    return str(third_side)


thirdSide = triangle_third_side(3.0, 4.0)
print(thirdSide)


# 运用python库
def numpy_triangle_third_side(side1, side2):
    third_side = numpy.sqrt(numpy.square(side1) + numpy.square(side2))
    return str(third_side)


print(numpy_triangle_third_side(3.0, 4.0))


# 梯形面积函数
def trapezoid_area(base_up, base_down, height=3):
    return 1/2 * (base_up + base_down) * height


# 位置参数传值方式
print(trapezoid_area(1, 2, 3))
# 关键词参数传值方式
print(trapezoid_area(base_up=1, base_down=2, height=3))

# 关键词参数调用
print(trapezoid_area(height=3, base_down=2, base_up=1))
# positional argument follows keyword argument
# print(trapezoid_area(height=3, base_down=2, 1))
# print(trapezoid_area(base_up=1, base_down=2, 3))
print(trapezoid_area(1, 2, height=3))

# 定义参数的默认值
print(trapezoid_area(1, 2))
print(trapezoid_area(1, 2, height=6))


# 一棵圣诞树
print('   *', '  * *', ' * * *', '   | ', sep='\n')
