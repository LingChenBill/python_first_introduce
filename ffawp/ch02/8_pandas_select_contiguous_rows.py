# Date:2020/5/22
# Author:Lingchen
# Mark: 使用pandas选取持续的行（丢弃掉头部和尾部行）
#       python 8_pandas_select_contiguous_rows.py
#       data/supplier_data_unnecessary_header_footer.csv data/output/8_output_pandas.csv
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

# 丢弃不需要的行
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])

# 使用iloc函数根据行索引选取一个单独行作为索引
data_frame.columns = data_frame.iloc[0]
# 使用reindex函数为数据框重新生成索引
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)
