# Date:2020/5/9
# Author:Lingchen
# Mark: 读取4个数据文件至列表，并在屏幕上打印

# 列表
james = []
julie = []
mikey = []
sarah = []


# 读取文件数据
def read_file_data(file_name, train_list):
    try:
        with open(file_name, 'r') as fd:
            # for each_line in fd:
            #     each_line = each_line.strip()
            #     each_data = each_line.split(',')
            #     train_list.append(each_data)
            data = fd.readline()
            train_list = data.strip().split(',')
            print('Data: ', train_list)
            print('Sorted: ', sorted(train_list))

            # 清洗时间列表
            # clean_train_list = []
            # for each_item in train_list:
            #     clean_train_list.append(sanitize(each_item))

            # 列表推导：从右往左看（写）
            clean_train_list = [sanitize(each_item) for each_item in train_list]

            # 复制排序
            print('Sorted: ', sorted(clean_train_list))
    except IOError as err:
        print('File IO error: ', str(err))


# 清洗时间数据
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)


read_file_data('james.txt', james)
read_file_data('julie.txt', julie)
read_file_data('mikey.txt', mikey)
read_file_data('sarah.txt', sarah)


# print(james)
# print(julie)
# print(mikey)
# print(sarah)

