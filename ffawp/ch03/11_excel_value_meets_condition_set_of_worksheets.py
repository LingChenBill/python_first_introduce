# Date:2020/5/26
# Author:Lingchen
# Mark: 使用基础Python从第一个和第二个工作表中筛选出销售额大于$1900.00的那些行
#       python 11_excel_value_meets_condition_set_of_worksheets.py data/sales_2013.xlsx data/output/11_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

# 特定的sheet
my_sheets = [0, 1]
# 销售额阈值
threshold = 1900.0
# 销售额列索引
sales_column_index = 3
# 是否是第一个sheet的Flg
first_worksheet = True

with open_workbook(input_file) as workbook:
    data = []

    for sheet_index in range(workbook.nsheets):
        # 判断当前sheet索引是否是特定的索引
        if sheet_index in my_sheets:
            # 读取sheet
            worksheet = workbook.sheet_by_index(sheet_index)
            # 是否是第一页，处理标题行
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False

            # 处理数据行
            for row_index in range(1, worksheet.nrows):
                row_list = []
                # 销售额
                sale_amount = worksheet.cell_value(row_index, sales_column_index)

                # 销售额处理
                if sale_amount > threshold:
                    for column_index in range(worksheet.ncols):
                        cell_value = worksheet.cell_value(row_index, column_index)
                        cell_type = worksheet.cell_type(row_index, column_index)

                        # 日期列处理
                        if cell_type == 3:
                            date_cell = xldate_as_tuple(cell_value, workbook.datemode)
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
