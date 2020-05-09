# Date:2020/5/9
# Author:Lingchen
# Mark: 排序
#   原地排序
#   复制排序

data = [6, 3, 1, 2, 4, 5]
print('Data: ', data)

# 原地排序,sort()方法完成原声排序，这是每个Python列表都有的一个标准方法
data.sort()
print('Sort: ', data)

# 复制排序，使用sorted() BIF完成
data = [6, 3, 1, 2, 4, 5]
data2 = sorted(data)
print('Data2: ', data)
print('Sorted: ', data2)
