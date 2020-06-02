# Date:2020/6/2
# Author:Lingchen
# Mark: 从mysql数据表Suppliers数据表中查询出一组特定记录，然后将输出写入到CSV输出文件。
#       找出Cost列中的值大于700.00的所有记录，并将记录输出
#       python 5_db_mysql_write_to_file.py data/output_files/5_output.csv
import csv
import MySQLdb
import sys

# CSV输出文件名
output_file = sys.argv[1]

# 连接到Mysql数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='ffawp', passwd='Aa123456')
c = con.cursor()

# 创建写文件的对象，并写入标题行
file_writer = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
file_writer.writerow(header)

# 查询Suppliers表，并将结果写入CSV文件中
c.execute("""
    SELECT *
    FROM Suppliers
    WHERE Cost > 700.00;
""")

rows = c.fetchall()

for row in rows:
    file_writer.writerow(row)
