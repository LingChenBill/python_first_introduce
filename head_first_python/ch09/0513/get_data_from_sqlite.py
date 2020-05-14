# Date:2020/5/13
# Author:Lingchen
# Mark: 从sqlite3中获取数据
import sqlite3

db_name = 'coachdata.sqlite'


def get_names_from_store():
    """
    从sqlite数据库的athletes表中获取姓名信息
    :return:
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # 抽取数据
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()

    return response


# result_name = get_names_from_store()
# print(result_name)


def get_names_id_from_store():
    """
    从sqlite数据库的athletes表中获取姓名和ID信息
    :return:
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()

    return response


result_name = get_names_id_from_store()
print(result_name)


def get_athlete_from_id(athlete_id):
    """
    获取与指定id相关的计时数据
    :param athlete_id:
    :return:
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""", (athlete_id,))

    (name, dob) = results.fetchone()

    results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""", (athlete_id,))

    data = [row[0] for row in results.fetchall()]

    connection.close()

    response = {
        'name': name,
        'dob': dob,
        'data': data,
        'top3': data[0:3]
    }

    return response


result_timing = get_athlete_from_id(2)
print(result_timing)
