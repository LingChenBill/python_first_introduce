# Date:2020/5/2
# Author:Lingchen
# Mark: 递归汉诺塔问题:盘子移动问题


def hanoi(n, source, target, helper):
    if n == 1:
        print(str(n) + " : ", source + ' -> ' + target)
    else:
        hanoi(n - 1, source, helper, target)
        print(str(n) + " : ", source + ' -> ' + target)
        hanoi(n - 1, helper, target, source)


hanoi(4, 'A', 'B', 'C')
