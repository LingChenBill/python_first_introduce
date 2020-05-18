# Date:2020/5/18
# Author:Lingchen
# Mark: 在有序序列中用bisect查找某个元素的插入位置
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        # 用特定的bisect函数来计算元素应该出现的位置
        position = bisect_fn(HAYSTACK, needle)
        # 利用该位置来算出需要几个分隔符号
        offset = position * '  |'
        # 把元素和其应该出现的位置打印出来
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    # 根据命令上最后一个参数来选用bisect函数
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        # bisect函数其实是bisect_right的别名
        bisect_fn = bisect.bisect

    # 把选定的函数在抬头打印出来
    print('DEMO: ', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


# bisect可以用来建立一个用数字作为索引的查询表格
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    # i = bisect.bisect(breakpoints, score)
    i = bisect.bisect_left(breakpoints, score)
    return grades[i]


print('grade score: ', [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
