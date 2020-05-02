# Date:2020/4/28
# Author:Lingchen
# Mark: 传统列表-链表的实现
# 双向链表的各个节点中还需要持有一个指向前一节点的引用
# Python中list是一整块一连续的内存区块--通常称为数组（array）
import time


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


L = Node("a", Node("b", Node("c", Node("d"))))
print(L.next.next.value)

# 代码块的复杂度由其先后执行的语句累加而成的。而嵌套循环的复杂度则在此基础上成倍增长。
start = time.clock()

seq = range(10 ** 2)
s = 0
for x in seq:
    for y in seq:
        s += x * y

print("s: ", s)

end = time.clock()

print("running time: ", end - start)