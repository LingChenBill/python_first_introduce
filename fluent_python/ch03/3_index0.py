# Date:2020/5/21
# Author:Lingchen
# Mark: 从索引中获取单词出现的频率信息，并把它们写进对应的列表中
#       创建一个从单词到其出现情况的映射
#       python 3_index0.py data/zen.txt
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        print('line no: ', line_no)
        for match in WORD_RE.finditer(line):
            word = match.group()
            # print('word: ', word)
            column_no = match.start() + 1
            location = (line_no, column_no)
            # # 提取word出现的情况，若还没有它的记录，返回[]
            # occurrences = index.get(word, [])
            # # 把单词新出现的位置添加到列表的后面
            # occurrences.append(location)
            # # 把新的列表放回字典中，这又牵扯到一次查询操作
            # index[word] = occurrences

            # 使用dict.setdefault来实现
            # 获取单词的出现情况列表，若单词不存在，把单词和一个空列表放进映射，然后返回这个空列表。
            # 这样就可以在不进行第二次查询的情况下更新列表了
            index.setdefault(word, []).append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])

