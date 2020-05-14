# Date:2020/5/13
# Author:Lingchen
# Mark: 创建coachdata. 包含athletes和timing_data表
import sqlite3

# 创建连接
connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

# 创建表athletes
cursor.execute("""
  CREATE TABLE athletes(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    dob DATE NOT NULL
  ) """)

# 创建表timing_data
cursor.execute("""
  CREATE TABLE timing_data(
    athlete_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (athlete_id) REFERENCES athletes
  )""")

# 提交
connection.commit()
connection.close()
