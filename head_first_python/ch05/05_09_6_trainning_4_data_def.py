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


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print('james: ', james)
print('james set: ', sorted(set([float(sanitize(t)) for t in james]), reverse=True)[0:3])

print('julie: ', julie)
print('julie set: ', sorted(set([float(sanitize(t)) for t in julie]), reverse=True)[0:3])
print('mikey: ', mikey)
print('mikey set: ', sorted(set([float(sanitize(t)) for t in mikey]), reverse=True)[0:3])
print('sarah: ', sarah)
print('sarah set: ', sorted(set([float(sanitize(t)) for t in sarah]), reverse=True)[0:3])
