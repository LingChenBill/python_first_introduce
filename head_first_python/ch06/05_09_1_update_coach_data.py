# Date:2020/5/9
# Author:Lingchen
# Mark: 读取4个数据文件至列表，并在屏幕上打印

# 列表
james = []
julie = []
mikey = []
sarah = []


# 读取文件数据
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        return data.strip().split(',')
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
(james_name, james_dob) = james.pop(0), james.pop(0)
print(james_name + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in james]))[0:3]))

sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
