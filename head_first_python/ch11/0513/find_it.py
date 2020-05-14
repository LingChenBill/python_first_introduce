# Date:2020/5/14
# Author:Lingchen
# Mark: 从input读入数据，匹配最近的数据
import time


def find_closest(look_for, target_data):

    def whats_the_difference(first, second):
        if first == second:
            return 0
        elif first > second:
            return first - second
        else:
            return second - first

    max_diff = 9999999
    for each_thing in target_data:
        diff = whats_the_difference(each_thing, look_for)
        if diff == 0:
            found_it = each_thing
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each_thing
    return found_it


def time2secs(time_string):
    """
    将时间字符串转换成数字
    :param time_string:
    :return:
    """
    (hours, mins, secs) = time_string.split(':')
    seconds = int(secs) + (int(mins)*60) + (int(hours)*60*60)
    return seconds


def secs2time(seconds):
    """
    将时间数字转换成格式化的时间字符串
    :param seconds:
    :return:
    """
    return time.strftime('%H:%M:%S', time.gmtime(seconds))


# 测试匹配
# print("find_closest 1: ")
# print(find_closest(3.3, [1.5, 2.5, 4.5, 5.2, 6]))
#
# print("find_closest 2: ")
# print(find_closest(3, [1, 5, 6]))
#
# print("find_closest 3: ")
# print(find_closest(3, [1, 3, 4, 6]))
#
# print("find_closest 4: ")
# print(find_closest(3.6, [1.5, 2.5, 4.5, 5.2, 6]))
#
# print("find_closest 5: ")
# print(find_closest(3, [1, 4, 6]))
#
# print("find_closest 6: ")
# print(find_closest(2.6, [1.5, 2.5, 4.5, 5.2, 6]))
#
# print("find_closest 7tm2secs2tm.py: ")
# print(find_closest('59:59', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))





