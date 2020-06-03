# Date:2020/6/3
# Author:Lingchen
# Mark: 如何使用CSV输入文件更新Mysql数据表中已有的记录
#       python 6_db_mysql_update_from_csv.py data/data_for_updating_mysql.csv
import csv
import MySQLdb
import sys

# CSV输入文件
input_file = sys.argv[1]
# 连接Mysql
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='ffawp', passwd='Aa123456')
c = con.cursor()

# 读取CSV文件
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
# 读取（去掉）标题行
header = next(file_reader, None)

for row in file_reader:
    data = []

    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)

    # Update语句中需要几个值，变需要几个%s占位符表示出查询中的值的位置
    # CSV输入文件中数据的顺序也要同查询中属性的顺序一样
    c.execute("""
        UPDATE Suppliers SET Cost=%s, Purchase_Date=%s
        WHERE Supplier_Name=%s;
    """, data)

con.commit()

# 查询Suppliers表
c.execute("SELECT * FROM Suppliers")

rows = c.fetchall()

for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)

