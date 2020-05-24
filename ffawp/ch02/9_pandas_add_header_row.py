# Date:2020/5/22
# Author:Lingchen
# Mark: 使用pandas选取持续的行（丢弃掉头部和尾部行）
#       python 9_pandas_add_header_row.py data/supplier_data_no_header_row.csv data/output/9_output_pandas.csv
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 标题列
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']

# read_csv函数可以直接指定输入文件不包含标题行，并可以提供一个列标题列表
data_frame = pd.read_csv(input_file, header=None, names=header_list)

data_frame.to_csv(output_file, index=False)
