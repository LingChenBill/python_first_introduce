# Date:2020/5/20
# Author:Lingchen
# Mark: 内存视图其实是泛化和去数学化的NumPy数组
#       它让你在不需要复制内容的前提下，在数据结构之间共享内存。
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print('numbers 1: ', numbers)
memv = memoryview(numbers)
print('len(memv): ', len(memv))
print('memv: ', memv)
print('memv[0]: ', memv[0])

memv_oct = memv.cast('B')
print('memv_oct.tolist(): ', memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

