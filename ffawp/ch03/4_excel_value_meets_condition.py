# Date:2020/5/24
# Author:Lingchen
# Mark: 运用基础Python来筛选出Sale Amount大于$1400.00行
#       python 4_excel_value_meets_condition.py data/sales_2013.xlsx data/output/4_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')

    # 将用输入文件中要写入输出文件中的那些行来填充这个列表
    data = []
    # 标题行处理
    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        row_list = []
        # 销售额
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)

        # 取出销售额 > 1400.0
        if sale_amount > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)

                # 日期行处理
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)

        # 只将非空的row_list加入到data列表中
        if row_list:
            data.append(row_list)

    # print('data: ', data)
    for list_index, output_list in enumerate(data):
        # print('list_index: ', list_index)
        # print('output_list: ', output_list)
        for element_index, element in enumerate(output_list):
            # print('ele_index: ', element_index)
            # print('ele: ', element)
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
