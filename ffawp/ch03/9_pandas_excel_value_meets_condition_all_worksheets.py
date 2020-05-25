# Date:2020/5/25
# Author:Lingchen
# Mark: 要使用pandas在所有工作表中筛选出销售额大于$2000.00的所有行
#       python 9_pandas_excel_value_meets_condition_all_worksheets.py
#       data/sales_2013.xlsx data/output/9_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=False)
row_output = []

for worksheet_name, data in data_frame.items():
    # data['Sale Amount'].astype(float) > 2000.0) 结果是行索引，data[行索引]就可以取出对应的行
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])

filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.close()
