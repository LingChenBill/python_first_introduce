# Date:2020/5/17
# Author:Lingchen
# Mark: 对序列使用 + 和 *
#       + 和 * 都遵循：不修改原有的操作对象，而是构建一个全新的序列

l = [1, 2, 3]
print('l * 5: ', l * 5)
print('l: ', l)

print('5 * abcd: ', 5 * 'abcd')

# 井字游戏块，一个包含3个列表的列表，嵌套的3个列表各自有3个元素来代表井字游戏的一行方块
board = [['_'] * 3 for i in range(3)]
print('board: ', board)
board[1][2] = 'X'
print('board 2: ', board)

# 外面的列表其实包含3个指向同一个列表的引用。
weird_board = [['_'] * 3] * 3
print('weird_board: ', weird_board)

weird_board[1][2] = 'X'
print('weird_board 2: ', weird_board)

# 指向同一个引用对象
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
print('board 3: ', board)
board[1][2] = 'X'
print('board 3: ', board)

# 每次迭代中都新建了一个列表，作为新的一行（row）追加到游戏板中
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print('board 4: ', board)
board[1][2] = 'X'
print('board 4: ', board)

