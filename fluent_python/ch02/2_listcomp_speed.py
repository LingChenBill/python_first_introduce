# Date:2020/5/16
# Author:Lingchen
# Mark: map/filter组合起来，与列表推导比，执行速度
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp: ', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func: ', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('listcomp + lambda: ', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('listcomp + func: ', 'list(filter(non_ascii, map(ord, symbols)))')


