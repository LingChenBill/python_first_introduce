# Date:2020/5/31
# Author:Lingchen
# Mark: 创建数据库sqlite3中的数据表，在表插入数据，以及在输出中获取数据并对行进行计数
import sqlite3

# 使用专用名称':memory:'在内存中创建了一个数据库
con = sqlite3.connect(":memory:")

# 创建表sales字符串
query = """
  CREATE TABLE sales
  (customer VARCHAR(20),
   product VARCHAR(40),
   amount FLOAT,
   date DATE);
"""

# 执行query中的SQL命令
con.execute(query)
# commit()方法将修改提交到数据库
con.commit()

# 在表中插入几行数据
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]

# INSERT语句
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
# executemany()方法执行4次INSERT语句，高效率地将4行数据插入sales表
con.executemany(statement, data)
con.commit()

# 查询sales表
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# 计算查询结果中行的数量
row_counter = 0
for row in rows:
        print(row)
        row_counter += 1

print('Number of rows: %d' % row_counter)
