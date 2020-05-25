# Date:2020/5/24
# Author:Lingchen
# Mark: 对Excel表格内容的日期进行格式化
#       python 3_excel_parsing_and_write_keep_dates.py data/sales_2013.xlsx data/output/3_output.xlsx
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')

    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            # print('cell type: ', worksheet.cell_type(row_index, col_index))
            # 单元格类型为3：表示这个单元格中包含日期数据
            if worksheet.cell_type(row_index, col_index) == 3:
                # xldate_as_tuple函数将Excel中代表日期、时间或日期时间的数值转换为元组
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                # print('date cell: ', date_cell)
                # date cell:  (2013, 1, 1, 0, 0, 0)

                # 格式化日期内容
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)

output_workbook.save(output_file)
