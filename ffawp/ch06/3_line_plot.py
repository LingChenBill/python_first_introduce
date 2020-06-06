# Date:2020/6/6
# Author:Lingchen
# Mark: 拆线图中的数值点在一条拆线上。它通常用来表示数值随着时间发生的变化
#       python 3_line_plot.py
import matplotlib.pyplot as plt
from numpy.random import randn

plt.style.use('ggplot')

# 使用randn创建绘图所用的随机数据
plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()

fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)

# 每条折线都可以通过选项进行设置，使用不同的数据点类型、颜色和线型
ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')

# 为统计图创建图例，loc='best'指示matplotlib根据图中的空白部分将图例放在最合适的位置
plt.legend(loc='best')

plt.savefig('data/output_files/line_plot.png', dpi=400, bbox_inches='tight')
plt.show()

