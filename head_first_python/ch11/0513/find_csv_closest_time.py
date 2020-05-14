# Date:2020/5/14
# Author:Lingchen
# Mark: 查找csv中最近匹配的数据
from find_it import find_closest
from tm2secs2tm import time2secs, secs2time


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


# 测试时间数据
print("find_nearest_time 1: ")
print(find_nearest_time('59:59', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))

print("find_nearest_time 2: ")
print(find_nearest_time('1:01:01', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))

print("find_nearest_time 3: ")
print(find_nearest_time('1:02:01', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))

print("find_nearest_time 4: ")
print(find_nearest_time('57:06', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))

