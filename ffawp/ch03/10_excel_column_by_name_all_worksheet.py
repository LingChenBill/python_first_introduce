# Date:2020/5/26
# Author:Lingchen
# Mark: 使用基础Python在所有工作表中选取Customer Name和Sale Amount列
#       python 10_excel_column_by_name_all_worksheet.py data/sales_2013.xlsx data/output/10_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')

# 特定标题列
my_columns = ['Customer Name', 'Sale Amount']
# 是否第一个sheet页Flg
first_worksheet = True

with open_workbook(input_file) as workbook:
    data = [my_columns]
    # 待保存的特定列索引
    index_of_cols_to_keep = []

    for worksheet in workbook.sheets():
        if first_worksheet:
            header = worksheet.row_values(0)
            for column_index in range(len(header)):
                if header[column_index] in my_columns:
                    index_of_cols_to_keep.append(column_index)

            # 第一个sheet页Flg置为False
            first_worksheet = False

        # 每一个sheet页中循环所有的数据行
        for row_index in range(1, worksheet.nrows):
            row_list = []

            # 每一行循环特定的数据列
            for column_index in index_of_cols_to_keep:
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
