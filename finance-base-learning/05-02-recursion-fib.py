# Date:2020/5/2
# Author:Lingchen
# Mark: 递归f(n) = f(n-1) + f(n-2)


def fib(n):
    if n < 0:
        raise ValueError
    elif n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print("1: ", fib(1))
print("2: ", fib(2))
print("3: ", fib(3))
# 值越大，递归的执行效率太低
print("40: ", fib(40))


