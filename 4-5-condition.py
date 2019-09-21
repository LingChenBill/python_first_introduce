# Date:2019/9/21
# Author:Lingchen
# Mark:
#   条件控制
#   如果if后面的布尔表达式过长或者难于理解，可以采取给变量赋值的办法来储存布尔表达式返回的布尔值True或者False
#   多条件判断同样很简单，只需在if和else之间增加上elif，用法和if是一致的


def account_login():
    password = input('Password:')
    password_correct = password == '12345'
    # if password == '12345':
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()


# account_login()

password_list = ['*#*#', '12345']
def account_login_multis():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login_multis()
    else:
        print('Wrong password or invalid input!')
        account_login_multis()


account_login_multis()