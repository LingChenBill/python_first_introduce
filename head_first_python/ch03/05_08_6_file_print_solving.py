# Date:2020/5/8
# Author:Lingchen
# Mark: 通过自定义模块lc_nester来输出列表到指定文件
import lc_nester

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

    # 并行处理，使用，号隔开
    with open('man_data_nester.txt', 'w') as man_file, open('other_data_nester.txt', 'w') as other_file:
        # print(man, file=man_file)
        # print(other, file=other_file)
        lc_nester.print_lol(man, out=man_file)
        lc_nester.print_lol(other, out=other_file)


except IOError as err:
    print('File Error: ', str(err))
