# Date:2020/5/12
# Author:Lingchen
# Mark: JSON库的使用
import json

# 创建一个包含列表的列表（多重列表）
names = ['John', ['Johnny', 'Jack'], 'Michael', ['Mike', 'Mikey', 'Mick']]
print('name: ', names)

# 将Python多重列表转换为一个JSON多重列表
to_transfer = json.dumps(names)
print('to_transfer: ', to_transfer)

# 将JSON多重列表转换回Python能理解的格式
from_transfer = json.loads(to_transfer)
print('from_transfer: ', from_transfer)

