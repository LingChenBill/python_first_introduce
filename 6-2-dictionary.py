# Date:2019/9/22
# Author:Lingchen
# Mark:
#   字典: 名称-内容进行数据的构建, 键-值对
#       字典中数据必须是以键值对的形式出现的
#       逻辑上讲，键是不能重复的，而值是可以重复的
#       字典中的键是不可变的，也就是无法修改的，而值是可变的，可修改的，可以是任何对象

NASDAO_code = {
    'BIDU': 'Baidu',
    'SINA': 'Sina',
    'YOKU': 'Yoku'
}
print(NASDAO_code)

# 将一个可变的的元素作为key来构建字典
# key_test = {[]: 'a Test'}
# print(key_test)

# 相同的键值也只能出现一次
a = {'key':123, 'key':123}
print(a)

# 添加元素
NASDAO_code['ALIBABA'] = 'Alibaba'
print(NASDAO_code)

# 添加多个元素
NASDAO_code.update({'FB': 'Facebook', 'TELA': 'Tesla'})
print(NASDAO_code)

# 删除字典中的元素
del NASDAO_code['FB']
print(NASDAO_code)
print(NASDAO_code['TELA'])

# 字典是不能够切片的
# print(NASDAO_code[1:4])

