#! /usr/bin/env python3
# 保留发票编号由”001-“开头的行，并将结果写入一个输出文件
# python 5_csv_reader_value_matches_pattern.py data/supplier_data.csv data/output/5_output.csv
import csv
import sys
import re

input_file = sys.argv[1]
output_file = sys.argv[2]

# r表示将单引号之间的模式当作原始字符串来处理
# ?P<my_pattern_group>捕获了名为<my_pattern_group>的组中匹配了的子字符串，以便以后打印到屏幕或者是写入文件
# 搜索的实际模式：^001-.*
# re.I: 大小写敏感的匹配
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        # 处理标题
        header = next(file_reader)
        file_writer.writerow(header)

        for row_list in file_reader:
            # 发票
            invoice_number = row_list[1]
            # 匹配查找
            if pattern.search(invoice_number):
                print(row_list)
                file_writer.writerow(row_list)
