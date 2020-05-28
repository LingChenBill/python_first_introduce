# Date:2020/5/27
# Author:Lingchen
# Mark: 知道一个文件夹中工作簿的数量，每个工作薄中工作表的数量，以及每个工作表中行与列的数量
#       python 12_excel_introspect_all_workbooks.py data
import glob
import sys
import os
from xlrd import open_workbook

input_directory = sys.argv[1]
workbook_counter = 0

# 循环文件夹里的Excel文件
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
    workbook = open_workbook(input_file)
    # 文件名
    print('Workbook: %s' % os.path.basename(input_file))
    # 工作表数量
    print('Number of worksheets: %d' % workbook.nsheets)

    # 循环文件表
    for worksheet in workbook.sheets():
        print('Worksheet name: ', worksheet.name, '\tRows: ', worksheet.nrows,
              '\tColumns: ', worksheet.ncols)
    workbook_counter += 1

print('Number of Excel workbooks: %d' % workbook_counter)
