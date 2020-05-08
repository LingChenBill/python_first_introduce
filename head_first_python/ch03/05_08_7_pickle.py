# Date:2020/5/8
# Author:Lingchen
# Mark: 使用pickle模块，使用dump()保存数据，使用load()恢复数据

import pickle

# "b"告诉python以二进制模式打开数据文件
with open('mydata.pickle', 'wb') as mysavedata:
    # dump()保存数据
    pickle.dump([1, 2, 'three'], mysavedata)

with open('mydata.pickle', 'rb') as myrestoredata:
    # load()从文件恢复数据
    a_list = pickle.load(myrestoredata)

print(a_list)
