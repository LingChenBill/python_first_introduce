# Date:2020/5/9
# Author:Lingchen
# Mark: 读取4个数据文件至列表，排序后，放至字典数据结构中, 将处理细节放至函数中

# 字典
james = {}
julie = {}
mikey = {}
sarah = {}


# 读取文件数据
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        file_list = data.strip().split(',')

        # data_dic = dict()
        # data_dic['name'] = file_list.pop(0)
        # data_dic['birthday'] = file_list.pop(0)
        # # data_dic['time'] = file_list
        # data_dic['time'] = str(sorted(set([sanitize(t) for t in file_list]))[0:3])
        # return data_dic
        return {
            'name': file_list.pop(0),
            'birthday': file_list.pop(0),
            'time': str(sorted(set([sanitize(t) for t in file_list]))[0:3])
        }
    except IOError as err:
        print('File IO error: ', str(err))
        return None


# 清洗时间数据
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)

    return mins + '.' + secs


james = get_coach_data('james2.txt')
print('james: ', james)
print(james['name'] + "'s faster times are: " + james['time'])

julie = get_coach_data('julie2.txt')
print('julie: ', julie)
print(julie['name'] + "'s faster times are: " + julie['time'])

mikey = get_coach_data('mikey2.txt')
print('mikey: ', mikey)
print(mikey['name'] + "'s faster times are: " + mikey['time'])

sarah = get_coach_data('sarah2.txt')
print('sarah: ', sarah)
print(sarah['name'] + "'s faster times are: " + sarah['time'])
