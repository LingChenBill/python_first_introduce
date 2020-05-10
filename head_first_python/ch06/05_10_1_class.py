# Date:2020/5/10
# Author:Lingchen
# Mark: 类的定义，初始化


# 定义类
class Athlete:
    def __init__(self, value=0):
        self.thing = value

    # 扩充方法，返回thing的长度
    def how_big(self):
        return len(self.thing)


# 类的使用
d = Athlete('Holy Grail')
print(d.thing)
print(d.how_big())
