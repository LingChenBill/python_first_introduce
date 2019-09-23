# Date:2019/9/22
# Author:Lingchen
# Mark:
#   集合中的元素是无序的，不重复的任意对象，可以通过集合去判断数据的从属关系，也可以通过集合把数据结构中重复的元素减掉
#   集合不能被切片也不能被索引

a_set = {1, 2, 3, 4}
a_set.add(5)
a_set.discard(3)
print(a_set)

lyric = 'The night begin to shine, the night begin to shine'
words = [word for word in lyric.split()]
print(words)
words_index = set(words)
print(words_index)
counts_dict = {index: words.count(index) for index in words_index}
print(counts_dict)