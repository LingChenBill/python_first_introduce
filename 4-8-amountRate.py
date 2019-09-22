# Date:2019/9/22
# Author:Lingchen
# Mark:
#   复利计算函数，包含三个参数: amount(资金),rate(利率), time(时间)
#   公式: F = P * (1 + i)^n


def invest(amount, rate, time):
    count = 1
    while count < time:
        output = amount * (1 + rate) ** count
        print('Year %s: ' % str(time), output)
        count = count + 1


invest(100, 0.05, 9)

