# Date:2019/9/21
# Author:Lingchen
# Mark:
#   传入参数name与msg就可以在桌面写入的文件名称和内容的函数
#   定义一个为函数text_filter的函数，传入参数word, censored_word和changed_word实现过滤
#   创建一个文件可以在其中输入文字，但是如果信息中有敏感词的话将会被默认过滤后写入文件，参数name与信息参数msg


def text_create(name, msg):
    folder_path = '/Users/zhuyangze/Documents/fork/python_first_introduce/data/'
    full_path = folder_path + name + '.txt'
    # open函数要打开一个完整的路径
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('file write done!')


text_create('4-2-text-create', 'Hello function!')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


print(text_filter('Python is lame'))


def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)


censored_text_create('4-2-censored-text-create', 'lame!lame!lame! Python')
