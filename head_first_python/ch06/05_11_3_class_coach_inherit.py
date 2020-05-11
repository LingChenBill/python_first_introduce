# Date:2020/5/11
# Author:Lingchen
# Mark: 利用继承重写coach Athlete类，继承列表


class AthleteList(list):
    """
    初始化选手信息
    """
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        # 利用列表
        self.extend(a_times)

    def top3(self):
        """
        获取最快的3个运动时间
        :return:
        """
        # 数据本身是计时数据，不再需要times属性
        return sorted(set([sanitize(t) for t in self]))[0:3]


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
    获取选手运动数据
    :param file_name:
    :return:
    """
    try:
        with open(file_name) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as err:
        print("File error: " + str(err))
        return None


# 测试
# vera = AthleteList('vera vi')
# vera.append('1.31')
# print(vera.name)
# print("vera's first top3: ", vera.top3())
# # 既然从内置的list继承，所以可以使用list的方法来完成工作
# vera.extend(['2.22', '1-21', '2:21'])
# print("vera's second top3: ", vera.top3())

james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
