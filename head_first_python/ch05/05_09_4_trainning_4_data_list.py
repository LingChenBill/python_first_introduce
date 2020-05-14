# Date:2020/5/9
# Author:Lingchen
# Mark: 读取4个数据文件至列表，并在屏幕上打印


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


# 列表
james = []
julie = []
mikey = []
sarah = []

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))

print('James slice: ', james[0:3])

# 降顺排列列表
james = sorted([sanitize(t) for t in james], reverse=True)
# 删除列表中的重复项目
unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)

print("unique_james: ", unique_james)
print("unique_james slice: ", unique_james[0:3])

julie = sorted([sanitize(t) for t in julie], reverse=True)
# 删除列表中的重复项目
unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)

print("unique_julie: ", unique_julie)
print("unique_julie slice: ", unique_julie[0:3])

mikey = sorted([sanitize(t) for t in mikey], reverse=True)
# 删除列表中的重复项目
unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)

print("unique_mikey: ", unique_mikey)
print("unique_mikey slice: ", unique_mikey[0:3])

sarah = sorted([sanitize(t) for t in sarah], reverse=True)
# 删除列表中的重复项目
unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)

print("unique_sarah: ", unique_sarah)
print("unique_sarah slice: ", unique_sarah[0:3])

# 使用集合来去重
print('james set: ', sorted(set([sanitize(t) for t in james]), reverse=True)[0:3])
print('julie set: ', sorted(set([sanitize(t) for t in julie]), reverse=True)[0:3])
print('mikey set: ', sorted(set([sanitize(t) for t in mikey]), reverse=True)[0:3])
print('sarah set: ', sorted(set([sanitize(t) for t in sarah]), reverse=True)[0:3])
