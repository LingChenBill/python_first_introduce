# Date:2020/5/3
# Author:Lingchen
# Mark: timeit模块本身就是为执行相对可靠的计时操作而设计的。
# 当没有把握的时候，就用蛮力试试

import timeit


print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("x = sum(range(10))"))
