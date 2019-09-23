# Date:2019/9/23
# Author:Lingchen
# Mark:
#   类的继承


class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))


coke_CocaCola_China = CocaCola('可口可乐')
print(coke_CocaCola_China.local_logo)
coke_CocaCola_China.drink()


# 继承父类: CocaCola
class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color'
    ]


coke_caffeine = CaffeineFree('Cocacola-FREE')
print(coke_caffeine.local_logo)
print(coke_caffeine.caffeine)
coke_caffeine.drink()