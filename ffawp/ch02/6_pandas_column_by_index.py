# Date:2020/5/22
# Author:Lingchen
# Mark: 使用pandas根据索引值选取列
#       python 6_pandas_column_by_index.py data/supplier_data.csv data/output/6_output_pandas.csv
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

# iloc函数来根据索引位置选取列
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(output_file, index=False)
