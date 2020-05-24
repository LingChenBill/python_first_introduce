# Date:2020/5/24
# Author:Lingchen
# Mark: 利用pandas来实现计算每个文件中值的总和与均值
import pandas as pd
import glob
import sys
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)

    # 销售额总计，sum()函数
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))
                               for value in data_frame.loc[:, 'Sale Amount']]).sum()

    # 销售额均值，mean()函数
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))
                                 for value in data_frame.loc[:, 'Sale Amount']]).mean()

    # 组装数据
    data = {
        'file_name': os.path.basename(input_file),
        'total_sales': total_cost,
        'average_sales': average_cost
    }

    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

# 每个文件数据从上到下组装
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)
