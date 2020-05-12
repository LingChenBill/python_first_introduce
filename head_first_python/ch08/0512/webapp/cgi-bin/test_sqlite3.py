# Date:2020/5/12
# Author:Lingchen
# Mark: 测试sqlite3模块
import sqlite3

# 建立与数据库的连接
connection = sqlite3.connect('test.sqlite')
# 创建数据游标
cursor = connection.cursor()
# 执行一些sql操作
cursor.execute("""SELECT DATE('NOW')""")
# 提交做出的修改，使修改永久保存
connection.commit()
# 完成时关闭连接
connection.close()
