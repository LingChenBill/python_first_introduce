# Date:2019/9/23
# Author:Lingchen
# Mark:
#   在美国，所有人喝到的可乐都是一样的，无论是总统或者是流浪汉
#   在Python中，class来类比
#   类是有一些系列有共同特征和行为事物的抽象概念的总和
#   在类里面赋值的变量就是类的变量，而类的变量有一个专有的术语，称为类的属性
#   类的实例化，被实例化的对象，称之为实例
#   类属性引用
#   在创建类后，通过object.new_attr的形式进行一个赋值，就得到了一个新的实例的变量-实例属性
#   Python的类中存在一些方法，被称为"魔术方法"，如__init__()

class CocaCola:
    it_taste = 'So good'


coke_for_bum = CocaCola()
coke_for_president = CocaCola()

print(coke_for_bum.it_taste)
print(coke_for_president.it_taste)


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    # self其实就是被创建的实例本身，就是将一个个对象作为参数放入函数括号内
    def drink(self):
        print('Energy!')


coke_for_me = CocaCola()
coke_for_you = CocaCola()
print(CocaCola().formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

for element in coke_for_me.formula:
    print(element)

coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'
print(coke_for_China.local_logo)
coke_for_China.drink()

coke = CocaCola()
print(coke.drink() == CocaCola.drink(coke))


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def drink(self, how_much):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache!')


ice_coke = CocaCola()
ice_coke.drink('a sip')


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    # __init__(self) 初始化操作
    def __init__(self):
        self.local_logo = '可口可乐'

        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')


coke_China = CocaCola()
print(coke_China.local_logo)

class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    # __init__(self) 初始化操作
    def __init__(self, logo_name):
        self.local_logo = logo_name

        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')


coke_init = CocaCola('中国可口可乐')
print(coke_init.local_logo)
coke_init.drink()
