#! /usr/bin/env python3
# 使用基础Python选取特定行
# python 8_csv_reader_select_contiguous_rows.py
# data/supplier_data_unnecessary_header_footer.csv data/output/8_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 行索引
row_counter = 0

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        for row in file_reader:
            print(row_counter, [value.strip() for value in row])
            # 去掉不需要的行和尾部行
            if 3 <= row_counter <= 15:
                file_writer.writerow([value.strip() for value in row])
            row_counter += 1
