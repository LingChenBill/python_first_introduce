# Date:2020/5/13
# Author:Lingchen
# Mark: 从input读入数据，匹配最近的数据
from find_it import find_closest
from tm2secs2tm import time2secs, secs2time, format_time


def find_nearest_time(look_for, target_data):
    """
    查找的时间以及所搜索的时间列表，这个函数将把找到的最接近的时间作为一个字符串返回
    :param look_for:
    :param target_data:
    :return:
    """
    # 将要查找的时间字符串转换为等价的秒数值
    what = time2secs(look_for)
    print(what)
    # 将时间字符串行转换为秒数
    where = [time2secs(t) for t in target_data]
    print(where)
    # 查找最近的匹配的时间
    res = find_closest(what, where)
    # 返回时间字符串
    return secs2time(res)


row_data = {}

# 处理数据文件
with open('data/PaceData.csv') as paces:
    # 标题行处理，去空白符，分割成列表
    column_headings = paces.readline().strip().split(',')
    # 去除第一列
    column_headings.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        # 将时间放至对应的标签列表中
        # row_data[row_label] = row

        inner_dict = {}
        for i in range(len(column_headings)):
            # 键：时间，值：列标题；快速地确定与某个时间关联的列
            inner_dict[format_time(row[i])] = column_headings[i]

        row_data[row_label] = inner_dict

# print(row_data)

# input()函数
# help(input)
distance_run = input('Enter the distance attempted: ')
recorded_time = input('Enter the recorded time: ')
predicted_distance = input('Enter the distance you want a prediction for: ')

# 报KeyError错误，因为row_data没有对应的key与value
# print(row_data[distance_run][recorded_time])

closest_time = find_nearest_time(format_time(recorded_time), row_data[distance_run])
print('closest_time: ', closest_time)
closest_time_heading = row_data[distance_run][closest_time]
print('closest_time_heading: ', closest_time_heading)

prediction = [k for k in row_data[predicted_distance].keys()
              if row_data[predicted_distance][k] == closest_time_heading]

print('The predicted time running ' + predicted_distance + ' is: ' + prediction[0] + '.')
