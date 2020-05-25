# Date:2020/5/25
# Author:Lingchen
# Mark: 使用列标题来筛选Excel中的特定列
#       python 8_excel_column_by_name.py data/sales_2013.xlsx data/output/8_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 指定列标题
my_columns = ['Customer Name', 'Purchase Date']

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_columns]

    header_list = worksheet.row_values(0)
    header_index_list = []

    # 根据特定列标题找出对应的列索引
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)

    for row_index in range(1, worksheet.nrows):
        row_list = []

        # 只筛选特定的指定列数据
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)

            # 处理日期数据
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
