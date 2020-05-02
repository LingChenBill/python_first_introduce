# Date:2020/5/2
# Author:Lingchen
# Mark: 计算100以内的数字和
# 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。


def my_sum(i):
    if i < 0:
        raise ValueError
    elif i <= 1:
        return i
    else:
        return i + my_sum(i - 1)


print("sum 10: ", my_sum(10))
print("sum 100: ", my_sum(100))
