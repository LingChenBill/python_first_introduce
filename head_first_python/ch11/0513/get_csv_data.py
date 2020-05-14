# Date:2020/5/13
# Author:Lingchen
# Mark: 从CSV数据读取原始数据

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
            inner_dict[row[i]] = column_headings[i]

        row_data[row_label] = inner_dict

# num_cols = len(column_headings)
# print(num_cols, end=' -> ')
# print(column_headings)
#
# num_2mi = len(row_data['2mi'])
# print(num_2mi, end=' -> ')
# print(row_data['2mi'])
#
# num_Marathon = len(row_data['Marathon'])
# print(num_Marathon, end=' -> ')
# print(row_data['Marathon'])

print(dir())

# 尝试找出与15k行上的时间43.24相关联的列标题，然后使用这个列标题找到跑20公里的预测时间
# column_heading = row_data['15k']['43:24']
# print(column_heading)
#
# print(row_data['20k'].keys())
# print(row_data['20k'])
# prediction = [k for k in row_data['20k'].keys() if row_data['20k'][k] == column_heading]
# print(prediction)

print("条件列表推导：")
times = [t for t in row_data['Marathon'].keys()]
print(times)

print("times other: ")
times = []
for each_t in row_data['Marathon'].keys():
    times.append(each_t)
print(times)

print("条件列表推导2：")
headings = [h for h in sorted(row_data['10mi'].values(), reverse=True)]
print(headings)
print("headings other: ")
headings = []
for each_t in sorted(row_data['10mi'].values(), reverse=True):
    headings.append(each_t)
print(headings)

print("条件列表推导3：")
print(row_data['20k'])
time = [t for t in row_data['20k'].keys() if row_data['20k'][t] == '79.3']
print(time)
print("time other: ")
time = []
for each_t in row_data['20k'].keys():
    if row_data['20k'][each_t] == '79.3':
        time.append(each_t)
print(time)
