# Date:2020/5/13
# Author:Lingchen
# Mark: 从现有的模型取得选手数据，并将数据加载到新创建的SQLite数据中
import sqlite3
import glob
import athletemodel

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

# 加载数据
data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob

    # 使用insert语句向athletes表增加新的数据行
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    connection.commit()

    cursor.execute("SELECT id FROM athletes WHERE name = ? AND dob = ?", (name, dob))

    # fetchone()返回的是一个列表
    the_current_id = cursor.fetchone()[0]

    for each_time in athletes[each_ath].clean_data:
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (the_current_id, each_time))

    connection.commit()

connection.close()


