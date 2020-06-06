# Date:2020/6/6
# Author:Lingchen
# Mark: 箱线图可以表示出数据的最小值、第一四分位数、中位数、第三四分位数和最大值
#       正态分布和对数正态分布数据的箱线图
#       python 5_box_plot.py
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
index_value = np.random.random_integers(low=0, high=N - 1, size=N)

normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]

box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# 创建列表标签
box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']

# notch=False表示箱体是矩形，sym='.'表示离群点是圆点，vert=True表示箱体是垂直的
# showmeans=True表示箱体在显示中位数的同时也显示均值
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')

plt.savefig('data/output_files/box_plot.png', dpi=400, bbox_inches='tight')
plt.show()
