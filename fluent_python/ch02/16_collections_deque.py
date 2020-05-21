# Date:2020/5/20
# Author:Lingchen
# Mark: collections.deque类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
#       deque可以在多线程程序中安全地当作先进先出的栈使用
from collections import deque

dq = deque(range(10), maxlen=10)
print('dq: ', dq)

# 队列的旋转操作，当n > 0时，队列的最右边的n个元素会被移动到队列的左边。当n < 0时，最左边的n个元素会被移动到右边
dq.rotate(3)
print('dq.rotate(3): ', dq)

dq.rotate(-4)
print('dq.rotate(-4): ', dq)

# 当试图对一个已满的队列做尾部添加操作的时候，它头部的元素会被删除掉
dq.appendleft(-1)
print('dq.appendleft(-1): ', dq)

# 添加已满的元素时，会挤掉另外一端的元素
dq.extend([11, 22, 33])
print('dq.extend([11, 22, 33]): ', dq)

dq.extendleft([10, 20, 30, 40])
print('dq.extendleft([10, 20, 30, 40]): ', dq)



