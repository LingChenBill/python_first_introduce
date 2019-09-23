# Date:2019/9/23
# Author:Lingchen
# Mark:
#   类属性与实例属性
#   __dict__是一个类的特殊属性，它是一个字典，用于储存类或者实例的属性，是默认隐藏的
#   Python中属性的引用机制是自外而内的
#   Python中任何种类的对象都是类的实例
#   类的背后所承载的理念是OOP(面向对象)的编程理念，在大型项目中为了易于管理和维护代码质量，会采取面向对象的方式，也是软件工程的智慧所在

from bs4 import BeautifulSoup


class TestA:
    attr = 1

    def __init__(self):
        self.attr = 42


obj_A = TestA()
obj_B = TestA()
print(obj_A.attr)
print(obj_B.attr)
print(TestA.__dict__)
print(obj_A.__dict__)

# TestA.attr = 42
obj_A.attr = 43
print(obj_A.attr)
print(obj_B.attr)
print(TestA.__dict__)
print(obj_A.__dict__)

# 内建类型
obj1 = 1
obj2 = 'String'
obj3 = []
obj4 = {}
print(type(obj1), type(obj2), type(obj3), type(obj4))

soup = BeautifulSoup
print(type(soup))


