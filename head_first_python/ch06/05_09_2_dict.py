# Date:2020/5/9
# Author:Lingchen
# Mark: 字典

# 创建字典
cleese = {}
palin = dict()
print("cleese's type: ", type(cleese))
print("palin's type: ", type(palin))

# 字典赋值
cleese['name'] = 'John Cleese'
cleese['occupations'] = ['actor', 'comedian', 'writer', 'film producer']

palin = {'name': 'Michael Palin', 'occupations': ['comedian', 'actor', 'writer', 'tv']}
print("cleese's value: ", cleese)
print("palin's value: ", palin)

# 访问字典数据
print(cleese['name'])
print(cleese['occupations'][-1])
# 不包括分片后项的数据
print(cleese['occupations'][-3: -1])

# 可以动态扩展来存储额外的键/值对
palin['birthplace'] = 'Broomhill, Sheffield, England'
cleese['birthplace'] = 'Weston-super-Mare, North Somerset, England'

# 字典不会维持插入的顺序，关于字典，重点是它会维护关联关系，而不是顺序
print('palin: ', palin)
print('cleese: ', cleese)

