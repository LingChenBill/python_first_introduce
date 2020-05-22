#! /usr/bin/env python3
# 通过列索引值来获取列数据
# python 6_csv_reader_column_by_index.py data/supplier_data.csv data/output/6_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 想保留的两列的索引值
my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        for row_list in file_reader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            file_writer.writerow(row_list_output)
