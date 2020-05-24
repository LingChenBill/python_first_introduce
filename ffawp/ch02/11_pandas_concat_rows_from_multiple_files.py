# Date:2020/5/23
# Author:Lingchen
# Mark: 运用pandas来连接多个文件（csv）的数据行至一个文件中
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)

# axis=0表示从头到尾垂直堆叠，axis=1表示并排地平行堆叠
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
# data_frame_concat = pd.concat(all_data_frames, axis=1, ignore_index=True)
# data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=False)
data_frame_concat.to_csv(output_file, index=False)
