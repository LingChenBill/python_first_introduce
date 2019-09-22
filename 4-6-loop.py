# Date:2019/9/22
# Author:Lingchen
# Mark:
#   for循环: 于...其中的每一个元素，做...事情
#   range函数: 可以得到一个具有连续整数的序列
#   歌曲列表中有三首歌'Holy Diver','Thunderstruck','Rebel Rebel',当播放到每首时，分别显示对应的歌手名字'Dio','AC/DC','David Bowie'
#   嵌套循环: 九九乘法口诀表
#   while循环: 只要...条件成立，就一直做...
#   死循环
#   在循环过程中制造某种可以使循环停下来的条件
#   让while循环停下来的另一种方法: 改变使循环成立的条件
#   给登录函数增加一个新功能: 输入密码错误超过3次就禁止再次输入密码

for every_letter in 'Hello world':
    print(every_letter)


for num in range(1, 11):
    print(str(num) + ' + 1 = ', num + 1)


songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song, ' - Dio')
    elif song == 'Thunderstruck':
        print(song, ' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song, ' - David Bowie')

for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i * j))

count = 0
while True:
    print('Repeat this line!')
    count = count + 1
    if count == 5:
        break

password_list = ['*#*#', '12345']

def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print(tries, 'Times left')
    else:
        print('Your account has bean suspended!')


account_login()
