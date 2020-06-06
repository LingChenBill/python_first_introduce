# Date:2020/6/6
# Author:Lingchen
# Mark: 创建一个频率分布图
#       直方图用来表示数值分布。
#       常用的直方图包括频率分布、频率密度分布、概率分布和概率密度分布
#       python 2_histogram.py
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15

# 使用Python的随机数生成器创建两个正态分布变量x1和x2
x1 = mu1 + sigma * np.random.randn(10000)
x2 = mu2 + sigma * np.random.randn(10000)
fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)

# 创建两个频率分布图
# bins=50表示每个变量的值应该被分为50份，normed=False表示直方图显示的是频率分布
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Numbers of Values in Bin')

# 为基础图添加一个居中的标题
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
# 为子图添加一个居中的标题
ax1.set_title('Two Frequency Distributions')

plt.savefig('data/output_files/histogram.png', dpi=400, bbox_inches='tight')
plt.show()
