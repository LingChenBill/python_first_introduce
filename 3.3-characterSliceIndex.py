# Date:2019/9/21
# Author:Lingchen
# Mark:
#   字符串可以通过string[x]的方式进行索引、分片
#   字符串的分片(slice)实际上可以看作是从字符串中找出来你要截取的东西
#   :两边分别代表着字符串的分割从哪里开始，从哪里结束，包含开始，不包含结束
#   过长的代码段可以使用'\'来进行换行，属于一行的代码同时会有一个缩进代表是一行的

name = 'My name is Mike'

print(name[0])

print(name[-4])

print(name[11:14])
print(name[11:15])

print(name[5:])

print(name[:5])

# 找出你朋友中魔鬼
word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

# 解析爬虫后的图片地址，以一个统一的方式进行重命名:以链接尾部倒数10个字符的方式进行命名
url = 'https://pic2.zhimg.com/v2-b889f28b6ee7b0092997d703efb3bde1.jpg'
file_name = url[-10:]
print(file_name)

# 为了保护用户的信息安全性，通常账号信息只会显示后四位，其余的用"*"来代替
phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

# 来模拟手机通讯簿中的电话号码联想功能
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

# 字符串格式化
sentence = '{} a word she can get what she {} for.'
print(sentence.format('With', 'came'))

sentence = '{preposition} a word she can get what she {verb} for.'
print(sentence.format(preposition='With', verb='came'))

sentence = '{0} a word she can get what she {1} for.'
print(sentence.format('With', 'came'))

# 字符串填空的方式
city = input('write down the name of city:')
url = 'http://apistore.baidu.com/microservice/weather?citypinyin={}'.format(city)
print(url)