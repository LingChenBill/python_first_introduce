# Date:2020/6/6
# Author:Lingchen
# Mark: 散点图表示两个数值变量之间的相对关系，有助于识别出变量之间是否具有正相关或负相关
#       python 4_scatter_plot.py
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

x = np.arange(start=1., stop=15., step=1.)
# print(x)
# 通过随机数使数据与一条直线和一条二次曲线稍稍偏离
# y_linear = x + 5. * np.random.randn(14.)
# TypeError: 'float' object cannot be interpreted as an integer
y_linear = x + 5. * np.random.randn(14)
y_quadratic = x ** 2 + 10. * np.random.randn(14)

# 使用numpy的poly1d函数通过两组数据点(x, y_linear)和(x, y_quadratic)拟合出一条直线与一条二次曲线
# poly1d函数可以使用这些系数创建实际的多项式方程
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))

fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)

# 'bo'表示(x, y_linear)点是蓝色圆圈，'go'表示(x, y_quadratic)点是绿色圆圈
# 'b-'表示(x, y_linear)点之间的线是一条蓝色实线，'g-'表示(x, y_quadratic)点之间的线是一第绿色实线
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Scatter Plots Regression Lines')

plt.xlabel('x')
plt.ylabel('f(x)')

# 设置了x轴与y轴的范围
# plt.xlim(0, 20)
# plt.ylim(0, 200)
plt.xlim((min(x) - 1., max(x) + 1.))
plt.ylim((min(y_quadratic) - 10., max(y_quadratic) + 10.))

plt.savefig('data/output_files/scatter_plot.png', dpi=400, bbox_inches='tight')
plt.show()
