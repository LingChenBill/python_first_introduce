# Date:2020/5/24
# Author:Lingchen
# Mark: 使用基础Python筛选出Excel中客户姓名包含一个特定模式（以大写字母J开始）
#       python 6_excel_value_match_pattern.py data/sales_2013.xlsx data/output/6_output.xlsx
import sys
import re
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 特定模式
# r表示单引号之间的模式是一个原始字符串，正则是 ^J.*
pattern = re.compile(r'(?P<my_pattern>^J.*)')
# 姓名列索引
customer_name_index = 1

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    # 标题处理
    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        row_list = []
        # 姓名正则匹配筛选
        if pattern.search(worksheet.cell_value(row_index, customer_name_index)):
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
