# Date:2020/5/10
# Author:Lingchen
# Mark: 定义一个运动数据类
# 类的属性最好保存原始数据，需要计算得出的数据最好通过方法来实现，保持灵活与扩展
# 通常把代码与数据封装到一个定制类中。方便维护


class Athlete:
    """
    选手类，包含姓名，年龄，运动时间
    类的好处，更多功能 = 更多方法，如top3()
    """
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        """
        取出最快的三个时间
        格式化，去重，排序，转换成字符串
        :return: 返回最好是一个原始列表，你不知道调用者怎么处理这个列表，不要假设是字符串
        """
        # return str(sorted(set([sanitize(t) for t in self.times]))[0:3])
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self, a_time):
        """
        将一个额外的计时值追加到选手的计时数据
        :param a_time:
        :return:
        """
        self.times.append(a_time)

    def add_times(self, a_times):
        """
        会用一个或多个计时值（提供为一个列表），来扩展一个选手的计时数据
        运用extend方法
        :param a_times:
        :return:
        """
        self.times.extend(a_times)


def sanitize(time_string):
    """
    清洗时间数据
    :param time_string:
    :return:
    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)

    return mins + '.' + secs


def get_coach_data(file_name):
    """
    读取文本数据
    :param file_name:
    :return:
    """
    try:
        with open(file_name) as f:
            data = f.readline()
        # 去空白符，切割
        templ = data.strip().split(',')

        return Athlete(templ.pop(0), templ.pop(0), templ)
        # templ_name = templ.pop(0)
        # templ_dob = templ.pop(0)
        # templ_times = templ
        # print("templ's times: ", templ)
        # return Athlete(templ_name, templ_dob, templ_times)
    except IOError as err:
        print('File error: ' + str(err))
        return None


# 获取数据
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
# 输出
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

# 追加计时数据
james.add_time('2.13')
print(james.name + "'s add anther time: " + str(james.top3()))
james.add_times(['2.02', '2.12', '2:21'])
print(james.name + "'s add times: " + str(james.top3()))

vera = Athlete('vera vi')
vera.add_time('1.31')
# print(vera.top3())
print("vera's time: " + str(vera.top3()))
vera.add_times(['2.22', '1-21', '2:22'])
print("vera's times: " + str(vera.top3()))
