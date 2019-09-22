# Date:2019/9/22
# Author:Lingchen
# Mark:
#   打印1~100内的偶数

index = 0
while True:
    index = index + 1
    if index % 2 == 0:
        print('even: ' + str(index))
    elif index > 100:
        break
    # print(index)1