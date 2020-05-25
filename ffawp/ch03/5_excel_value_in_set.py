# Date:2020/5/24
# Author:Lingchen
# Mark: 使用基础Python筛选出Excel购买日期属于一个特定集合的行
#       python 5_excel_value_in_set.py data/sales_2013.xlsx data/output/5_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 筛选集合
important_dates = ['01/24/2013', '01/31/2013']
# 购买日期列索引
purchase_date_column_index = 4

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    # 标题处理
    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        # 购买日期处理
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index),
                                            workbook.datemode)
        purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')

        row_list = []
        # 购买日期集合筛选
        if purchase_date in important_dates:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)

                # 购买日期列判断处理
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 日期格式化
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)

for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
