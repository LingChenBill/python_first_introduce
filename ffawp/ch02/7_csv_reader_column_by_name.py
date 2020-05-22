#! /usr/bin/env python3
# 使用列标题来获取发票号码列和购买日期列
# python 7_csv_reader_column_by_name.py data/supplier_data.csv data/output/7_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 想保留的两列的列标题
my_columns = ['Invoice Number', 'Purchase Date']
# 想保留列的列索引
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')
        header = next(file_reader, None)

        # 处理标题列，记录列索引
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        file_writer.writerow(my_columns)

        for row_list in file_reader:
            row_list_output = []
            # 通过记录的列索引来获取数据
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            file_writer.writerow(row_list_output)
