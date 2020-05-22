#! /usr/bin/env python3
# 保留供应商名字为Supplier Z或成本大于￥600.00的行
# python 3_csv_reader_value_meets_condition.py data/supplier_data.csv data/output/3_output.csv
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        file_reader = csv.reader(csv_in_file, delimiter=',')
        file_writer = csv.writer(csv_out_file, delimiter=',')

        # 处理标题
        header = next(file_reader)
        file_writer.writerow(header)

        for row_list in file_reader:
            # 供应商
            supplier = str(row_list[0]).strip()
            # 成本(数据处理，去$,',')
            cost = str(row_list[3]).strip('$').replace(',', '')
            # 保留供应商名字为Supplier Z 或 成本大于￥600.00的行
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                print(row_list)
                file_writer.writerow(row_list)
