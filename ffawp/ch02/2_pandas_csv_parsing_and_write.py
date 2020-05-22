#! /usr/bin/env python3
# python 2_pandas_csv_parsing_and_write.py data/supplier_data.csv data/output/2_output.csv
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)

data_frame.to_csv(output_file, index=False)
