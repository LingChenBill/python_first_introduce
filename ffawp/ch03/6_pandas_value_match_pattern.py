# Date:2020/5/24
# Author:Lingchen
# Mark: 利用pandas筛选出Excel中客户姓名包含一个特定模式（以大写字母J开始）
#       python 6_pandas_value_match_pattern.py data/sales_2013.xlsx data/output/6_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013', index_col=None)

data_frame_value_match_pattern = data_frame[data_frame['Customer Name'].str.match('^J.*')]
# data_frame_value_match_pattern = data_frame[data_frame['Customer Name'].str.startswith('J')]
writer = pd.ExcelWriter(output_file)

data_frame_value_match_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.close()
