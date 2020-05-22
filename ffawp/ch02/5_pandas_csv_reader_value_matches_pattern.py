#! /usr/bin/env python3
# 保留发票开头”001-“开头的行
# python 5_pandas_csv_reader_value_matches_pattern.py data/supplier_data.csv data/output/5_output_pandas.csv
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

# 保留发票开头”001-“开头的行
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith('001-'), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)

