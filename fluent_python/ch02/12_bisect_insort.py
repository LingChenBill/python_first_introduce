# Date:2020/5/19
# Author:Lingchen
# Mark: 用bisect.insort插入新元素
#       排序很耗时，因此在得到一个有序序列之后，最好能够保持它的有序
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
