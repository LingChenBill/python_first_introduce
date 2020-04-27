# Date:2020/4/27
# Author:Lingchen
# Mark: 判断一个数是否是2的幂次方, 使用位运算


def is_pow2(n):
    return (n & (n - 1)) == 0


print("16: ", is_pow2(16))
print("32: ", is_pow2(32))
print("34: ", is_pow2(34))
