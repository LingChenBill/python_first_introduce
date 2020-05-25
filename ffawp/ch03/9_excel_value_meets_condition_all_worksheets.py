# Date:2020/5/25
# Author:Lingchen
# Mark: 要使用基础Python在所有工作表中筛选出销售额大于$2000.00的所有行
#       python 9_excel_value_meets_condition_all_worksheets.py data/sales_2013.xlsx data/output/9_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()

output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

# 销售额列索引
sales_column_index = 3
# 销售额阈值
threshold = 2000.0
# 第一个工作表Flg
first_worksheet = True

with open_workbook(input_file) as workbook:
    # 汇总数据列表
    data = []

    for worksheet in workbook.sheets():
        # 只在第一个sheet中处理标题行
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False

        # 处理标题行以外的数据行
        for row_index in range(1, worksheet.nrows):
            # 循环列数据列表
            row_list = []
            sale_amount = worksheet.cell_value(row_index, sales_column_index)

            # 筛选销售额处理
            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)

                    # 处理日期列
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list:
                data.append(row_list)

    # 将所有符合条件的数据写入新的excel中
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
