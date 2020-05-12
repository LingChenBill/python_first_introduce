#! /usr/bin/env python
# Date:2020/5/12
# Author:Lingchen
# Mark: 访问表单数据,启动CGI跟踪来帮助解决问题
import cgi
import athletemodel
import yate
import cgitb

# 启用python的CGI跟踪技术
cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete_name + ", DOB: " + athletes[athlete_name].dob + "."))

print(yate.para("The top times for this athlete are: "))
# print(yate.u_list(athletes[athlete_name].top3()))
# @property 类的属性调用方式改变
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "generate_list.py"}))
