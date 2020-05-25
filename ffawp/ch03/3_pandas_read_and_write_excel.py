# Date:2020/5/24
# Author:Lingchen
# Mark: 使用pandas读取Excel文件
#       python 3_pandas_read_and_write_excel.py data/sales_2013.xlsx data/output/3_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
writer = pd.ExcelWriter(output_file)

data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
