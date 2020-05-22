# Date:2020/5/22
# Author:Lingchen
# Mark: 使用pandas根据列标题选取列
#       python 7_pandas_column_by_name.py data/supplier_data.csv data/output/7_output_pandas.csv
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

# loc函数来根据列标题选取列
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)
