# Date:2020/5/2
# Author:Lingchen
# Mark: 函数传值设置
# 函数定义格式：默认参数
# 可变参数：*args,自动组装成tuple
# 关键字参数：**kvs, 自动组装成dict
# 命名关键字参数


def func(a, b, c=0, *args, **kvs):
    print(a, b, c)
    print(args)
    print(kvs)


print("1: ")
func(1, 2)

print("2: ")
func(1, 2, 3)

print("3: ")
func(1, 2, 3, 'a', 'b', 'c')

print("4: ")
func(1, 2, 3, 'a', 'b', 'c', china='BJ', uk='LD')

# 代码可读性
print("5: ")
func(1, 2, 3, *('a', 'b', 'c'), **{'china': 'BJ', 'uk': 'LD'})
