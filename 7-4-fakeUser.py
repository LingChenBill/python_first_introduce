# Date:2019/9/23
# Author:Lingchen
# Mark:
#   填充用户假数据的小工具
#   元组比列表要更省内存
#   生成器(generator),在函数中在任意一种循环中使用yield返回结果，就可以得到类似于range函数的效果

import random

ln_path = '/Users/zhuyangze/Documents/fork/python_first_introduce/data/first_name.txt'
fn_path = '/Users/zhuyangze/Documents/fork/python_first_introduce/data/last_name.txt'

fn = []
ln1 = []
ln2 = []

with open(fn_path, 'r') as f:
    for line in f.readlines():
        print(line.split('\n')[0])
        fn.append(line.split('\n')[0])
print(fn)
print('=' * 70)

with open(ln_path, 'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
print(ln1)
print('=' * 70)
print(ln2)

fn_tuple = tuple(fn)
ln1_tuple = tuple(ln1)
ln2_tuple = tuple(ln2)
print(fn_tuple)
print(ln1_tuple)
print(ln2_tuple)


class FakeUser:

    def fake_name(self, amount=1, one_word=False, two_word=False):
        n = 0
        while n <= amount:
            if one_word:
                # random.choice返回随机的一项
                full_name = random.choice(ln1) + random.choice(fn)
            elif two_word:
                full_name = random.choice(ln1) + random.choice(fn)
            else:
                full_name = random.choice(ln1 + ln2) + random.choice(fn)
            # print(full_name)
            yield full_name
            n += 1

    def fake_gender(self, amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '未知'])
            # print(gender)
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self, amount=1, few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 1000)
            # print(followers)
            yield followers
            n += 1


user_a = FakeUser()
user_b = SnsUser()
# for name in user_a.fake_name(30):
#     print(name)
# for gender in user_a.fake_gender(30):
#     print(gender)

for name, gender in zip(user_a.fake_name(30), user_a.fake_gender(30)):
    print(name, gender)

# user_a.fake_name()
# user_b.get_followers(few=True)
