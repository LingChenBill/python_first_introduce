# Date:2020/5/8
# Author:Lingchen
# Mark: 文件处理异常,一般使用with语句,就可以不用finally语句，来关闭文件流了。
# with语句使用了一种名为上下文管理协议（context management protocol）

try:
    with open('missing.txt', 'w') as data:
        print(data.readline(), end='')
except IOError as err:
    # 异常由except组处理时，显示这个异常信息
    # 可以使用str() BIF把异常对象转换（或强制转换）为字符串
    print('File Error: ' + str(err))

man = []
other = []

try:
    data = open('sketch.txt')
    # 使用with语句来处理文件
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                # 删除行中不需要的空白符
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print("The datafile is missing: ", str(err))

print('Man: ', man)
print('Other Man: ', other)

# 写入文件
try:

    # with处理文件写操作
    # with open('man_data.txt', 'w') as man_file:
    #     # 写入文件
    #     print(man, file=man_file)
    #
    # with open('other_data.txt', 'w') as other_file:
    #     print(other, file=other_file)

    # 并行处理，使用，号隔开
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)

except IOError as err:
    print('File Error: ', str(err))
