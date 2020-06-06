# Date:2020/6/5
# Author:Lingchen
# Mark: 统计客户在过去一年中购买的金、银、铜服务包，数据中包含客户购买服务包的购买日期或更新日期
#       使用Python字典数据结构来组织和保存计算结果，使用键-值对填充字典的便捷性
#       字典中的键是唯一的字符串，键-值对中的键和值由冒号分隔，每个键-值对之间由逗号分隔
#       python 2_calculate_statistic_by_category.py
#           data/customer_category_history.csv data/output_files/2_app_output.csv
import csv
import sys
from datetime import date, datetime


def date_diff(date_from, date_to):
    """
    计算开始日期与结束日期之间的差值（间隔的天数）
    :param date_from:
    :param date_to:
    :return:
    """
    try:
        # datetime.strptime()函数按照日期字段串创建datetime对象
        # print(datetime.strptime(date_from, '%m/%d/%Y') - datetime.strptime(date_to, '%m/%d/%Y'))
        # 输出日期52 days, 0:00:00
        diff = str(datetime.strptime(date_from, '%m/%d/%Y') - datetime.strptime(date_to, '%m/%d/%Y')).split()[0]
    except:
        diff = 0

    # 若两个日期相等
    if diff == '0:00:00':
        diff = 0

    return diff


input_file = sys.argv[1]
output_file = sys.argv[2]

# 数据字典
packages = {}

# 'N/A'不包括在输入列中
# 客户变量
previous_name = 'N/A'
# 服务包类别
previous_package = 'N/A'
# 服务包日期
previous_package_date = 'N/A'

# 是否处理输入文件中的第一行数据
first_row = True
# 当前日期
today = date.today().strftime('%m/%d/%Y')

with open(input_file, 'r', newline='') as input_csv_file:
    # csv读取对象
    file_reader = csv.reader(input_csv_file)
    # 标题
    header = next(file_reader)

    for row in file_reader:
        # 客户名
        current_name = row[0]
        # 服务包名称
        current_package = row[1]
        # 日期
        current_package_date = row[3]

        # 检验current_name的值是不是字典中键，否则加入
        if current_name not in packages:
            packages[current_name] = {}

        # 嵌套字典，客户名称-服务包-天数，如：{'John Smith': {'Bronze':0}}
        if current_package not in packages[current_name]:
            packages[current_name][current_package] = 0

        if current_name != previous_name:
            # 是否处理第一行数据（不处理）
            if first_row:
                first_row = False
            else:
                diff = date_diff(today, previous_package_date)

                if previous_package not in packages[previous_name]:
                    packages[previous_name][previous_package] = int(diff)
                else:
                    packages[previous_name][previous_package] += int(diff)

        else:
            diff = date_diff(current_package_date, previous_package_date)
            packages[previous_name][previous_package] += int(diff)

        previous_name = current_name
        previous_package = current_package
        previous_package_date = current_package_date

header = ['Customer Name', 'Category', 'Total Time（in Days）']

with open(output_file, 'w', newline='') as output_csv_file:
    file_writer = csv.writer(output_csv_file)
    file_writer.writerow(header)

    # 在外部字典和内部字典的键和值之间循环
    for customer_name, customer_name_value in packages.items():
        for package_category, package_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, package_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(package_category_value)
            file_writer.writerow(row_of_output)
