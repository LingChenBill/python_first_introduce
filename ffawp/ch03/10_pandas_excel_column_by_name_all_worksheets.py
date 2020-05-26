# Date:2020/5/26
# Author:Lingchen
# Mark: 使用pandas在所有工作表中选取Customer Name和Sale Amount列
#       python 10_pandas_excel_column_by_name_all_worksheets.py data/sales_2013.xlsx data/output/10_output_pandas.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
column_output = []

for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])

selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)

selected_columns.to_excel(writer, sheet_name='selected_columns_all_wroksheets', index=False)
writer.save()
