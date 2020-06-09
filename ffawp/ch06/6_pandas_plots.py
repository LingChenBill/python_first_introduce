# Date:2020/6/7
# Author:Lingchen
# Mark: 使用pandas数据框中的数据创建一对条形图和箱线图，并将它们并排放置
#       python 6_pandas_plots.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 创建了一个基础图和两个并排放置的子图
flg, axes = plt.subplots(nrows=1, ncols=2)
# 将两个子图分别赋于两个变量，就可以不用使用行和列的索引（如axes[0, 0]）
ax1, ax2 = axes.ravel()

print(np.random.rand(5, 3))
data_frame = pd.DataFrame(np.random.rand(5, 3),
                          index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                          columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metrics'))

# 创建一个条形图
data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar plot')
# 使用matplotlib的函数来设置x，y轴标签的旋转角度和字体大小
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 设置颜色字典
colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')
# 创建一个箱线图，并分别着色，并将离群点的形状设置为红色圆点
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box plot')

plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)

ax2.set_xlabel('Metric')
ax2.set_ylabel('Value')

ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.savefig('data/output_files/pandas_plots.png', dpi=400, bbox_inches='tight')
plt.show()
