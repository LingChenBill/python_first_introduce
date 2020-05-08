# Date:2020/5/8
# Author:Lingchen
# Mark: 使用模块pickle和自定义模块lc_nester来加载数据
import pickle
import lc_nester

new_man = []

try:
    # 以二进制读取文件
    with open('man_data_pickle.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

# 打印新的列表
lc_nester.print_lol(new_man)
print('New man list: ')
print(new_man[0])
print(new_man[-1])
