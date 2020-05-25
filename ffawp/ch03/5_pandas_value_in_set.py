# Date:2020/5/24
# Author:Lingchen
# Mark: 利用pandas筛选出Excel购买日期属于一个特定集合的行
#       python 5_pandas_value_in_set.py data/sales_2013.xlsx data/output/5_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013', index_col=None)

important_dates = ['01/24/2013', '01/31/2013']

data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]
writer = pd.ExcelWriter(output_file)

data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.close()