# Date:2020/5/8
# Author:Lingchen
# Mark: 代码持久化
# strip(): 删除空白符
# append(): 数据添加元素

man = []
other = []

try:
    data = open('sketch.txt')
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

    # 文件关闭
    data.close()

except IOError:
    print("The datafile is missing!")

print('Man: ', man)
print('Other Man: ', other)

# 写入文件
try:

    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    # 写入文件
    print(man, file=man_file)
    print(other, file=other_file)

except IOError:
    print('File Error!')

finally:

    # 如果在写入文件时出现IOError异常，执行finally
    # 关闭文件
    man_file.close()
    other_file.close()
