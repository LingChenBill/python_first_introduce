"""
BIF find()函数，
"""

import os

print('打开一个文本文件，并读取：')
data = open('sketch.txt')

for each_line in data:
    # if each_line.find(':') > 0 :
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

print("文件关闭：")
data.close()
