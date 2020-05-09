# Date:2020/5/9
# Author:Lingchen
# Mark: 列表推导示例

# 将分钟乘以60
mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print('secs: ', secs)

# 米转换成英尺
meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print('feet: ', feet)

# 将字符串转换成大写
lower = ['I', "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print('upper: ', upper)


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


clean = [sanitize(t) for t in ['2-22', '3:33', '4.44']]
print('clean: ', clean)
clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print('clean float: ', clean)
