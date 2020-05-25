# Date:2020/5/24
# Author:Lingchen
# Mark: 确定Excel工作薄的数量，名称和每个工作表中行列的数量
#       python 1_excel_introspect_workbook.py data/sales_2013.xlsx
import sys
from xlrd import open_workbook

input_file = sys.argv[1]

# 打开工作薄
workbook = open_workbook(input_file)
# 工作表的数量
print('Number of worksheets: ', workbook.nsheets)

for worksheet in workbook.sheets():
    # 工作表的名称，行，列的数量
    print('Worksheet name: ', worksheet.name, '\tRows: ', worksheet.nrows, '\tColumns: ', worksheet.ncols)
