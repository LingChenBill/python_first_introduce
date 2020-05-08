# Date:2020/5/8
# Author:Lingchen
# Mark: 将列表输出到文件或者到屏幕
import sys


def print_lol(the_list, indent=False, level=0, out=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, out)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=out)
            print(each_item, file=out)


# the_list = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
#             ["Graham Chapman",
#              ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# # print_lol(the_list, True)
#
# with open('nester.txt', 'w') as nester_file:
#     print_lol(the_list, True, out=nester_file)
