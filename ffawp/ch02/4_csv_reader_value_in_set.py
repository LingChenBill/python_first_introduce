#! /usr/bin/env python3
# 保留那些购买日期属于{'1/20/14', '1/30/14'}的行
# python 4_csv_reader_value_in_set.py data/supplier_data.csv data/output/4_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        # 处理标题
        header = next(file_reader)
        file_writer.writerow(header)

        for row_list in file_reader:
            a_date = row_list[-1]
            if a_date in important_dates:
                print(row_list)
                file_writer.writerow(row_list)
