# Date:2020/6/1
# Author:Lingchen
# Mark: 将数据从CSV文件中插入到数据表Suppliers
import csv
import MySQLdb
import sys
from datetime import datetime, date

# CSV输入文件的路径和文件名
input_file = sys.argv[1]
# 连接Mysql数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='ffawp', passwd='Aa123456')
c = con.cursor()

# 向Suppliers表中插入数据
file_reader = csv.reader(open(input_file, 'r', newline=''))
header = next(file_reader)

for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
        else:
            # 将csv中的日期字符串转换成日期
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            # print('a_date: ', a_date)
            # 将日期转换成特定格式的字符串
            a_date = a_date.strftime('%Y-%m-%d')

            data.append(a_date)
        print(data)

    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)

con.commit()

print('查询Suppliers表：')
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()

for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))

    print(row_list_output)

