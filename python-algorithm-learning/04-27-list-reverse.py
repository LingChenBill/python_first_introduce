# Date:2020/4/27
# Author:Lingchen
# Mark: 将数字添加到列表中，并反转
import time

# 先插入后，再反转
start = time.clock()
count = 10 ** 5
nums = []
for i in range(count):
    nums.append(i)

nums.reverse()
print(nums)
end = time.clock()
print("running time: ", end - start)

# 与其到最后才将列表整个反转，何不在数字出现的时候就将它插入到列表的头部 -> 速度变慢了，性能弹性也差了(相差200倍)
start = time.clock()
count = 10 ** 5
nums = []
for i in range(count):
    nums.insert(0, i)
print(nums)
end = time.clock()
print("running time: ", end - start)
