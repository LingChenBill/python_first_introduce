'''
#import nester: 使用命名空间，限定来访问nester函数
from nester import print_lol: 此种引入方法，print_lol函数会覆盖当前文件中同名的print_lol函数
'''

#import nester
from nester import print_lol

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']

# nester.print_lol(cast)
print_lol(cast)
