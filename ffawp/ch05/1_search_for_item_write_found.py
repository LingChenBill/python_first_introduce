# Date:2020/6/4
# Author:Lingchen
# Mark: 搜索file_archive文件夹，找出包含所需的数值项目的文件，
#       当找到一个数值项目时，需要把包含这个项目的整行数据写入输出文件
#       搜索文件为CSV和Excel文件
#       python 1_search_for_item_write_found.py
#           data/item_numbers_to_find.csv data/file_archive data/output_files/1_app_output.csv
import csv
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

# 提供搜索项的输入文件
item_numbers_file = sys.argv[1]
# 搜索文件夹
path_to_folder = sys.argv[2]
# 输出文件
output_file = sys.argv[3]

# 搜索项目
item_numbers_to_find = []

with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    file_reader = csv.reader(item_numbers_csv_file)

    for row in file_reader:
        item_numbers_to_find.append(row[0])

# ['1234', '2345', '4567', '6789', '7890']
# print(item_numbers_to_find)

# 输出文件
file_writer = csv.writer(open(output_file, 'a', newline=''))

# 文件计数
file_counter = 0
# 行号计数
line_counter = 0
# 项目统计
count_of_item_numbers = 0

for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
    # 处理的文件数 加1
    file_counter += 1

    # csv文件处理
    if input_file.split('.')[1] == 'csv':
        with open(input_file, 'r', newline='') as csv_in_file:
            file_reader = csv.reader(csv_in_file)
            # 去掉标题
            header = next(file_reader)

            for row in file_reader:
                row_of_output = []

                for column in range(len(header)):
                    # 金额列
                    if column == 3:
                        # 金额去 $ 和 , 和空格
                        cell_value = str(row[column]).lstrip('$').replace(',', '').strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)

                # 每一行加入当前文件名
                row_of_output.append(os.path.basename(input_file))

                if row[0] in item_numbers_to_find:
                    file_writer.writerow(row_of_output)
                    count_of_item_numbers += 1

                line_counter += 1

    # 处理Excel文件
    elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
        workbook = open_workbook(input_file)

        for worksheet in workbook.sheets():

            try:
                # 标题行
                header = worksheet.row_values(0)

            except IndexError:
                pass

            for row in range(1, worksheet.nrows):
                row_of_output = []

                for column in range(len(header)):

                    # 日期表格处理
                    if worksheet.cell_type(row, column) == 3:
                        # 取出日期数据
                        cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                        # 取年月日，去空格
                        cell_value = str(date(*cell_value[0:3])).strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(worksheet.cell_value(row, column)).strip()
                        row_of_output.append(cell_value)

                # 每一行数据加入当前文件名
                row_of_output.append(os.path.basename(input_file))
                # 工作表名
                row_of_output.append(worksheet.name)

                # 符合搜索条件的加入输出文件
                if str(worksheet.cell(row, 0).value).split('.')[0].strip() in item_numbers_to_find:
                    file_writer.writerow(row_of_output)
                    count_of_item_numbers += 1

                line_counter += 1

print('Number of file: ', file_counter)
print('Number of lines: ', line_counter)
print('Number of item numbers: ', count_of_item_numbers)

