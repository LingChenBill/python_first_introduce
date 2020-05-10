# Date:2020/5/10
# Author:Lingchen
# Mark: 定义一个运动数据类


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times


# 调用类，赋值类数据
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')

# sarah和james都由Athlete类的工厂函数创建，但它们存储在不同的内存地址上
print('Type sarah: ', type(sarah))
print('Type james: ', type(james))

print('sarah: ', sarah)
print('james: ', james)

# 使用点记法来访问与各个对象实例关联的属性
print("sarah's name: ", sarah.name)
print("james's name: ", james.name)
print("sarah's dob: ", sarah.dob)
print("james's dob: ", james.dob)
print("sarah's times: ", sarah.times)
print("james's times: ", james.times)
