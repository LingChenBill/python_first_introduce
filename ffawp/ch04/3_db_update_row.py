# Date:2020/5/31
# Author:Lingchen
# Mark: 如何使用CSV输入文件更新数据表中已有的记录
#       python 3_db_update_row.py data/data_for_updating.csv
import csv
import sys
import sqlite3

input_file = sys.argv[1]
# 创建sqlite3内存数据库和数据表sales
con = sqlite3.connect('data/db_update_row.db')
query = """
    CREATE TABLE IF NOT EXISTS sales
    (customer VARCHAR(20),
     product VARCHAR(40), 
     amount FLOAT,
     date DATE);
"""

con.execute(query)
con.commit()

# 向表中插入几行数据
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]

# 展示数据
for tuple_row in data:
    print(tuple_row)

statement = "INSERT INTO sales VALUES (?, ?, ?, ?)"
# 执行多条数据插入时使用executemany()
con.executemany(statement, data)
# con.execute(statement, data)
con.commit()

# 读取CSV文件并更新特定的行
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)

for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    # 为一组特定的customer更新amount值和date的值，列的顺序需要与csv中数据的顺序要一致
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)

con.commit()

# 查询更新后的记录
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
