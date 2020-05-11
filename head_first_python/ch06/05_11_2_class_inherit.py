# Date:2020/5/11
# Author:Lingchen
# Mark: 继承Python的内置list类。


class NamedList(list):
    """
    定义内置list类
    """
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NamedList("John Paul Jones")
print("johnny's type: ", type(johnny))

# 检查对象的类型（list）,看看它会提供什么内容
print(dir(johnny))

johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])
print("johnny's attr: ", johnny)
print("johnny's name: ", johnny.name)

# johnny是一个列表，可以对它做列表处理
for attr in johnny:
    print(johnny.name + " is a " + attr + ".")
