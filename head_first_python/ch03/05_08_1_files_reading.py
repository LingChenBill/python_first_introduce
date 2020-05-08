import os

print("当前工作目录:")
print(os.getcwd())

# print("切换目录：")
# os.chdir("/Users/zhuyangze/Documents/python/code/Head First Python/self")
# print(os.getcwd())

print('打开一个文本文件，并读取：')
data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')

print("循环遍历文件：")
data.seek(0)
# 针对python文件可以使用tell()方法
# data.tell()

for each_line in data:
    # print(each_line, end='')
    # 处理数据，split(), 额外的参数控制如何分割
    (role, line_spoken) = each_line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')

print("文件关闭：")
data.close()
