# Date:2020/5/23
# Author:Lingchen
# Mark: 从多个文件中连接数据
#       python 11_csv_reader_concat_rows_from_multiple_files.py
#       /Users/user_name/Documents/fork/python_first_introduce/ffawp/ch02/data data/output/11_output.csv
import glob
import csv
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True

for input_file in glob.glob(os.path.join(input_path, 'sales_*.csv')):
    print('file name: ', os.path.basename(input_file))

    with open(input_file, 'r', newline='') as csv_in_file:
        # 以'a'的模式打开写入文件，追加数据，'w'会覆盖以前的文件
        with open(output_file, 'a', newline='') as csv_out_file:
            file_reader = csv.reader(csv_in_file)
            file_writer = csv.writer(csv_out_file)

            if first_file:
                for row in file_reader:
                    file_writer.writerow(row)
                first_file = False
            else:
                # 去掉标题（非第一个文件）
                header = next(file_reader)
                for row in file_reader:
                    file_writer.writerow(row)
