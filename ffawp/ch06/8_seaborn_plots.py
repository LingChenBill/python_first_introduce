# Date:2020/6/7
# Author:Lingchen
# Mark: seaborn简化了在Python在创建信息丰富的统计图表的过程
#       它是在matplotlib基础上开发的，支持numpy和pandas中的数据结构，并集成了scipy和statsmodels中的统计程序
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig

sns.set(color_codes=True)

# 直方图
x = np.random.normal(size=100)
sns.distplot(x, bins=20, kde=False, rug=True, label="Histogram w/o Density")
sns.utils.axlabel("Value", "Frequency")

plt.title("Histogram of a Random Sample from a Normal Distribution")
plt.legend()
# plt.show()

# 带有回归直线的散点图与单变量直方图
mean, cov = [5, 10], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
data_frame = pd.DataFrame(data, columns=['x', 'y'])
# 使用jointplot函数显示两个变量的一张散点图，其中带有一条回归直线，并为每个变量生成一张直方图
sns.jointplot(x="x", y="y", data=data_frame, kind="reg").set_axis_labels("x", "y")
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")
# plt.show()

# 成对变量之间的散点图与单变量直方图
# iris = sns.load_dataset("iris")
# sns.pairplot(iris)
# plt.show()

# 按照某几个变量生成的箱线图
# tips = sns.load_dataset("tips")
# sns.factorplot(x="time", y="total_bill", hue="smoker", col="day", data=tips, kind="box", size=4, aspect=.5)
# plt.show()
# sns.lmplot(x="total_bill", y="tip", data=tips)

