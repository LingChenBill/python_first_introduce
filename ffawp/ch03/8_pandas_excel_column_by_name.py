# Date:2020/5/25
# Author:Lingchen
# Mark: 利用pandas来筛选特定的列(通过列标题的方式)
#       python3 8_pandas_excel_column_by_name.py data/sales_2013.xlsx data/output/8_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013', index_col=None)

data_frame_column_by_name = data_frame.loc[:, ['Customer Name', 'Purchase Date']]
writer = pd.ExcelWriter(output_file)

data_frame_column_by_name.to_excel(writer, sheet_name='jan_13_output', index=False)

writer.save()
