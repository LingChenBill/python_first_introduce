#! /usr/bin/env python3
# 保留那些购买日期属于{'1/20/14', '1/30/14'}的行
# python 4_pandas_csv_reader_value_in_set.py data/supplier_data.csv data/output/4_output_pandas.csv
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

# 购买日期集合
important_dates = ['1/20/14', '1/30/14', '2/17/14']

# 保留那些购买日期属于{'1/20/14', '1/30/14'}的行
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)

