# Date:2020/5/8
# Author:Lingchen
# Mark: 使用pickle模块来重写lc_nester自定义模块

import pickle

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

try:
    with open('man_data_pickle.txt', 'wb') as man_file, open('other_data_pickle.txt', 'wb') as other_file:
        # dump()保存数据
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

