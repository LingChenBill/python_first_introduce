# Date:2019/9/23
# Author:Lingchen
# Mark:
#   词频统计: 瓦尔登湖文本
#       有一些带标点符号的单词被单独统计了次数
#       有些单词不止一次的展示了出现的次数
#       由于Python对大小写敏感，开头大写的单词被单独统计了
import string

path = '/Users/zhuyangze/Documents/fork/python_first_introduce/data/Walden.txt'
# with open(path, 'r') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print('{} - {} times'.format(word, words.count(word)))

# 所有的标点符号
print(string.punctuation)

with open(path, 'r') as text:
    # 去掉连在一起的标点符号，并把首字母大写的单词转化为小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    # 将列表用set函数转换成集合，自动去除掉了其中所有重复的元素
    words_index = set(words)
    # 创建一个以单词为键(key)出现频率为值(value)的字典
    counts_dict = {index: words.count(index) for index in words_index}

# 以字典中的值为排序的参数(逆序)
for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{} - {} time'.format(word, counts_dict[word]))
