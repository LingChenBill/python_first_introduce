# Date:2019/9/21
# Author:Lingchen
# Mark:
#   单引号和双引号是一样的
#   '''xxxx''' 被用于过于长段的文字或者是说明，可以换行写下文字
#   不同的数据类型是不能够进行合并的
#   字符串可以相加，也可以相乘

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument

print(artist_intro)

num = 1
string = '1'
print(type(num))
print(type(string))
num2 = int(string)

# print(num + string)
print(num + num2)

words = 'words' * 3
print(words)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)