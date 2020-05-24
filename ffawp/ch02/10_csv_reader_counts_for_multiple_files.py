# Date:2020/5/23
# Author:Lingchen
# Mark: csv文件计数与文件中的行列计数
#       python 10_csv_reader_counts_for_multiple_files.py
#       /Users/user_name/Documents/fork/python_first_introduce/ffawp/ch02/data
import csv
import glob
import os
import sys

input_path = sys.argv[1]
file_counter = 0

# glob模块可以定位匹配于某个特定模式的所有路径名，可以匹配文件通配符（正则）
for input_file in glob.glob(os.path.join(input_path, '*.csv')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        file_reader = csv.reader(csv_in_file)
        header = next(file_reader, None)

        for row in file_reader:
            row_counter += 1

    # 打印出文件名，行数，列数
    print('{0!s}: \t{1:d} rows \t {2:d} columns'.format(
        os.path.basename(input_file), row_counter, len(header)
    ))

    file_counter += 1

print('Number of files: {0:d}'.format(file_counter))
