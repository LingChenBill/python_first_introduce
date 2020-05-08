fav_movies = ["The Holy Grail", "The life of Brian"]
print(fav_movies)
print(fav_movies[0])
print(fav_movies[1])

print("For 迭代列表:")
for each_flick in fav_movies:
    print(each_flick)
# 列表处理代码被称为“组”

print("也可考虑用while循环迭代:")
count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1

print("列表内嵌列表:")
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
print(movies[4][1][3])

print("遍历内嵌列表：")
for each_item in movies:
    print(each_item)

print("检查某个特定标识符:")
names = ['Michael', 'Terry']
print(isinstance(names, list))
num_names = len(names)
print(isinstance(num_names, list))

print("遍历内嵌列表-判断是否内嵌列表一：")
for each_item in movies:
    if isinstance(each_item, list):
        for item in each_item:
            print(item)
    else:
        print(each_item)

print("遍历内嵌列表-判断是否内嵌列表二：")
for each_item in movies:
    if isinstance(each_item, list):
        for item in each_item:
            if isinstance(item, list):
                for deep_item in item:
                    print(deep_item)
            else:
                print(item)
    else:
        print(each_item)

print("遍历内嵌列表-定义函数三：")
def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
print_lol(movies)
