# Date:2020/5/27
# Author:Lingchen
# Mark: 使用pandas 将多个工作簿中所有工作表中数据垂直连接成一个输出文件
#       python 13_pandas_excel_concat_data_from_multiple_workbook.py data data/output/13_output_pandas.xlsx
import pandas as pd
import glob
import sys
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = []

for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    # 循环工作表
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)

# 使用concat函数来连接数据框，垂直地堆叠起来，axis=0
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
