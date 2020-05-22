#! /usr/bin/env python3
# 保留供应商名字为Supplier Z或成本大于￥600.00的行
# python 3_pandas_csv_value_meets_condition.py data/supplier_data.csv data/output/3_output_pandas.csv
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

# 列Cost变换类型，用于比较大小
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

# 供应商名字为Supplier Z或成本大于￥600.00的行
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']
                                                   .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)

