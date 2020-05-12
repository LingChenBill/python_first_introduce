# Date:2020/5/11
# Author:Lingchen
# Mark: 为数据建模
import pickle


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

    @property
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


def put_to_store(files_list):
    """
    所有数据(从文本文件中获取)都存储在一个字典中
    :param files_list:
    :return:
    """
    # 字典
    all_athletes = {}
    for file in files_list:
        ath = get_coach_data(file)
        # 字典赋值: key-ath.name, value-AthleteList
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print("File error (put and store): " + str(err))

    return all_athletes


def get_from_store():
    """
    从字典中获取数据
    :return:
    """
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print("File error(put and store): " + str(err))

    return all_athletes


def get_names_from_store():
    """
    将选手名列表作为一个字符串返回
    :return:
    """
    athletes = get_from_store()
    response = [athletes[each_ath].name for each_ath in athletes]
    return response
