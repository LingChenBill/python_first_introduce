# Date:2020/5/8
# Author:Lingchen
# Mark: 文件处理异常

try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as err:
    # 异常由except组处理时，显示这个异常信息
    # 可以使用str() BIF把异常对象转换（或强制转换）为字符串
    print('File Error: ' + str(err))
finally:
    # locals() BIF会返回当前作用域中定义的所有名的一个集合
    if 'data' in locals():
        print('关闭文件：')
        data.close()
