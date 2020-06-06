# Date:2020/6/6
# Author:Lingchen
# Mark: 解析文本文件，将相关信息聚集起来，然后以合适的形式写入一个输出文件
#       使用Python代码来进行错误消息的分析和计算
#       python 3_parse_text_file.py data/mysql_server_error_log.txt data/output_files/3_app_output.csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 错误messages字典，结构如 {'2014-10-27': {'InnoDB: Using atomics to ref count buffer pool pages': 2}}
messages = {}
# 错误信息列表
notes = []

with open(input_file, 'r', newline='') as text_file:
    for row in text_file:
        # 只处理错误信息行
        if '[Note]' in row:
            # 按照空格将行进行拆分（最多拆分4次，分成5份）
            row_list = row.split(' ', 4)
            # 日期
            day = row_list[0].strip()
            # 错误信息
            note = row_list[4].strip('\n').strip()

            # 错误列表追加处理
            if note not in notes:
                notes.append(note)

            # 按照日期新建错误信息字典
            if day not in messages:
                messages[day] = {}

            # 按照错误信息进行统计
            if note not in messages[day]:
                messages[day][note] = 1
            else:
                messages[day][note] += 1

file_writer = open(output_file, 'w', newline='')
# 标题行
header = ['Date']
header.extend(notes)
# 将标题行每个字符串之间插入一个逗号，创建一个由逗号分隔各个值的长字符串
header = ','.join(map(str, header)) + '\n'
print(header)


file_writer.write(header)

for day, day_value in messages.items():
    # 空列表，保存写入输出文件的每行数据
    row_of_output = []
    row_of_output.append(day)

    for index in range(len(notes)):
        # 当前日期有此错误信息，则将计数加入，否则写入0
        if notes[index] in day_value.keys():
            row_of_output.append(day_value[notes[index]])
        else:
            row_of_output.append(0)

    output = ','.join(map(str, row_of_output)) + '\n'
    print(output)
    file_writer.write(output)

file_writer.close()
