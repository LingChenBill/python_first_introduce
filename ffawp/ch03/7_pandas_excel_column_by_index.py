# Date:2020/5/25
# Author:Lingchen
# Mark: 利用pandas来筛选特定的列
#       python3 7_pandas_excel_column_by_index.py data/sales_2013.xlsx data/output/7_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013', index_col=None)

# 如果使用iloc函数来选择列，那么就需要在列索引值前面加上一个冒号和一个逗号，
# 表示你想为这些特定的列保留所有的行，否则，iloc函数也会使用这些索引值去筛选行。
data_frame_column_by_index = data_frame.iloc[:, [1, 4]]
# data_frame_column_by_index = data_frame.iloc[[1, 4]]
writer = pd.ExcelWriter(output_file)

data_frame_column_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)

writer.save()
