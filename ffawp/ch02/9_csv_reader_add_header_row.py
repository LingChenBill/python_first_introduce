#! /usr/bin/env python3
# 使用基础Python添加列标题
# python 9_csv_reader_add_header_row.py data/supplier_data_no_header_row.csv data/output/9_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        # 标题列
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        # 写入标题
        file_writer.writerow(header_list)

        for row in file_reader:
            file_writer.writerow(row)
