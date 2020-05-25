# Date:2020/5/24
# Author:Lingchen
# Mark: 使用pandas筛选出满足特定条件的Excel行
#       python 4_pandas_value_meets_condition.py data/sales_2013.xlsx data/output/4_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# print(data_frame)
# print(data_frame['Sale Amount'].astype(float) > 1400.0)
# 筛选 销售额 > 1400.0 的行
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_2013', index=False)
writer.save()
