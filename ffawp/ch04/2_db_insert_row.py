# Date:2020/5/31
# Author:Lingchen
# Mark: 创建一个数据表，向表中插入CSV文件中的数据，然后展示表中数据
#       python 2_db_insert_row.py data/supplier_data.csv
import csv
import sqlite3
import sys

# csv文件名
input_file = sys.argv[1]

con = sqlite3.connect('data/Suppliers.db')
# 光标对象
c = con.cursor()

# 创建数据表Suppliers
create_table = """
    CREATE TABLE IF NOT EXISTS Suppliers
    (Supplier_Name VARCHAR(20),
     Invoice_Number VARCHAR(20),
     Part_Number VARCHAR(20),
     Cost FLOAT,
     Purchase_Date DATE);
"""

c.execute(create_table)
con.commit()

# 读取csv文件
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# 去除Header
header = next(file_reader, None)

# 插入数据
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)

    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
# 最后统一提交
con.commit()

print('查询Suppliers表：')
output = c.execute("SELECT * FROM Suppliers")
# 查询所有数据
rows = output.fetchall()

for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
