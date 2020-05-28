# Date:2020/5/26
# Author:Lingchen
# Mark: 使用pandas 从第一个和第二个工作表中筛选出销售额大于$1900.00的那些行
#       python 11_pandas_excel_value_meets_condition_set_of_worksheets.py
#       data/sales_2013.xlsx data/output/11_output_pandas.xlsx
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

# 特定的sheet
my_sheets = [0, 1]
# 销售额阈值
threshold = 1900.0

# 只获取特定sheet页的数据
data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)
row_list = []

for worksheet_name, data in data_frame.items():
    # 筛选销售额 > 1900.0的行
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])

# 重新拼接数据行
filtered_row = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_row.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()
