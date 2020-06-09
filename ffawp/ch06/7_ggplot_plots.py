# Date:2020/6/7
# Author:Lingchen
# Mark: ggplot与其他绘图包的关键区别是它的语法将数据与实际绘图明确地分离出来
#       ggplot提供了几种基本元素：几何对象、图形属性和标度
#       ggplot还提供了附加元素：统计变换、坐标系、子窗口和可视化主题
from ggplot import *
# print(mtcars.head())

# plt1 = ggplot(aes(x='mpg'), data=mtcars) +\
#         geom_histogram(fill='darkblue', binwidth=2) +\
#         xlim(10, 35) + ylim(0, 10) +\
#         xlab("MPG") + ylab("Frequency") +\
#         ggtitle("Histogram of MPG") +\
#         theme_gray()
# print(plt1)

# print(meat.head())
# plt2 = ggplot(aes(x='date', y='beef'), data=meat) +\
#     geom_line(color='purple', size=1.5, alpha=0.75) +\
#     stat_smooth(color='blue', size=2.0, span=0.15) +\
#     xlab("Year") + ylab("Head of Cattle Slaughtered") +\
#     ggtitle("Beef Consumption Over Time") +\
#     theme_gray()
# print(plt2)

print(diamonds.head())
# ggplot函数将数据集名称和图形属性都看作参数，以此来设置图形中各种具体变量
plt3 = ggplot(diamonds, aes(x='carat', y='price', colour='cut')) +\
    geom_point(alpha=0.5) +\
    scale_color_gradient(low='#05D9F6', high='#5011D1') +\
    xlim(0, 6) + ylim(0, 20000) +\
    xlab("Carat") + ylab("Price") +\
    ggtitle("Diamond Price by Carat and Cut") +\
    theme_gray()

print(plt3)
# ggsave(plt3, 'data/output_files/ggplot_plots.png')
