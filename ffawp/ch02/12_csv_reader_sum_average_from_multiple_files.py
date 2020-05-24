# Date:2020/5/24
# Author:Lingchen
# Mark: 计算每个文件中值的总和与均值
#       python 12_csv_reader_sum_average_from_multiple_files.py
#       /Users/user_name/Documents/fork/python_first_introduce/ffawp/ch02/data data/output/12_output.csv
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

# 输出文件标题列
output_header_list = ['file_name', 'total_sales', 'average_sales']
csv_out_file = open(output_file, 'a', newline='')
file_writer = csv.writer(csv_out_file)
# 写入标题列
file_writer.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        file_reader = csv.reader(csv_in_file)
        # 输出列表
        output_list = []
        # 文件名
        output_list.append(os.path.basename(input_file))
        # 去掉标题列
        header = next(file_reader)

        # 总计
        total_sales = 0.0
        # 销售数量
        numbers_of_sales = 0.0

        for row in file_reader:
            # 定位销售列
            sale_amount = row[3]
            # 去掉'$'和','，转换成数值累加
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            numbers_of_sales += 1
        # 均值
        average_sales = '{0:0.2f}'.format(total_sales/numbers_of_sales)

        output_list.append(total_sales)
        output_list.append(average_sales)
        # 写入每一个文件的总计与均值销售额
        file_writer.writerow(output_list)

# 关闭输出文件
csv_out_file.close()

