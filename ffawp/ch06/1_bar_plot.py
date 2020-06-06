# Date:2020/6/6
# Author:Lingchen
# Mark: 创建一个垂直条形图
#       使用matplotlib绘图时，首先要创建一个基础图，然后在基础图中创建一个或多个子图
#       python 1_bar_plot.py
import matplotlib.pyplot as plt

# 使用ggplot样式表来模拟ggplot2风格的图形
plt.style.use('ggplot')
# 为条形图准备数据
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
# 创建了一个客户索引列表
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]

# 创建一个基础图
fig = plt.figure()
# 向基础表中添加一个子图，创建1行1列的子图，并使用第一个也是唯一的一个子图
ax1 = fig.add_subplot(1, 1, 1)

# 创建条形图
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
# 设置刻度线位置在x轴底部和y轴左侧
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 将条形的刻度线标签由客户索引值更改为实际的客户名称
plt.xticks(customers_index, customers, rotation=0, fontsize='small')

# 设置x轴，y轴和标题标签
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

# 将统计图保存, bbox_inches='tight'表示在保存图形时，将图形四周的空白部分去掉
plt.savefig('data/output_files/bar_plot.png', dpi=400, bbox_inches='tight')
# plt.savefig('data/output_files/bar_plot.png')
plt.show()
