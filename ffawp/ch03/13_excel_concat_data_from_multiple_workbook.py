# Date:2020/5/27
# Author:Lingchen
# Mark: 使用基础Python将多个工作簿中所有工作表中数据垂直连接成一个输出文件
#       python 13_excel_concat_data_from_multiple_workbook.py data data/output/13_output.xlsx
import sys
import glob
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')

# 数据列表
data = []
# 是否是第一个工作表Flg
first_worksheet = True

# 循环工作薄
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    print('input_file: ', os.path.basename(input_file))

    # 处理工作簿
    with open_workbook(input_file) as workbook:
        # 循环处理工作表
        for worksheet in workbook.sheets():
            if first_worksheet:
                # 处理标题行
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False

            # 循环处理工作表的数据行
            for row_index in range(1, worksheet.nrows):
                row_list = []
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)

                    # 日期处理
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)

                data.append(row_list)

for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
