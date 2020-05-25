# Date:2020/5/24
# Author:Lingchen
# Mark: 使用基础Python和xlrd, xlwt模块读写Excel文件
#       python 2_excel_parsing_and_write.py data/sales_2013.xlsx data/output/2_output.xlsx
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

# 实例化一个xlwt的Workbook对象
output_workbook = Workbook()
# 运用add_sheet函数来为工作薄添加一个工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 打开输入的工作薄
with open_workbook(input_file) as workbook:
    # 打开工作表
    worksheet = workbook.sheet_by_name('january_2013')

    # 双循环来获取表格内容来写入输出工作表的内容
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))

# 保存并关闭输出工作薄
output_workbook.save(output_file)
