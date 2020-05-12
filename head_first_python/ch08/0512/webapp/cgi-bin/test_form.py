#! /usr/bin/env python
# Date:2020/5/12
# Author:Lingchen
# Mark: 测试生成一个input表单
import yate

print(yate.start_response('text/html'))
print(yate.do_form('add_timing_data.py', ['TimeValue'], text='Send'))
