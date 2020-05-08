"""
BIF try catch异常处理
pass: 可以把它认为是空语句或者是null语句
os模块有一些工具可以帮助确定一个数据文件是否存在
except ValueError: 指定特定异常处理
"""
import os

print('打开一个文本文件，并读取：')

# if os.path.exists('sketch.txt'):
try:
    data = open('sketch.txt')

    for each_line in data:
        # if each_line.find(':') > 0 :
        # if not each_line.find(':') == -1:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        # except:
        except ValueError:
            print('This is a error line!')
            pass

    print("文件关闭：")
    data.close()
# else:
# except:
except IOError:
    print('The data file is missing!')
