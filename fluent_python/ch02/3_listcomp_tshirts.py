# Date:2020/5/16
# Author:Lingchen
# Mark: 列表里是3种不同尺寸的T恤衫，每个尺寸都有2个颜色
#   列表推导的作用只有一个：生成列表

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# 得到的结果是先以颜色排列，再以尺码排列
tshirts = [(color, size) for color in colors for size in sizes]
print('tshirts color -> size: ', tshirts)

print('tshirts for: ')
for color in colors:
    for size in sizes:
        print((color, size))

# 依照先尺码后颜色的顺序来排列
tshirts = [(color, size) for size in sizes for color in colors]
print('tshirts size -> colors: ', tshirts)
