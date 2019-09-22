# Date:2019/9/22
# Author:Lingchen
# Mark:
#   设计一个函数，在data文件夹上创建10个文本，以数字给它们命名


def create_files(name, msg):
    forder_path = '/Users/zhuyangze/Documents/fork/python_first_introduce/data/'
    file_path = forder_path + name + '.txt'
    file = open(file_path, 'w')
    file.write(msg)
    file.close()


for i in range(1, 10):
    print(str(i) + ' file create!')
    create_files(str(i), 'The ' + str(i) + ' file contents!')
