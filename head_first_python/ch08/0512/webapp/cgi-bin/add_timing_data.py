#! /usr/bin/env python
# Date:2020/5/12
# Author:Lingchen
# Mark: 处理来自表单的数据
import cgi
import os
import time
import sys
import yate

print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())
print(host + ", " + addr + ", " + cur_time + ": " + method + ": ", end='', file=sys.stderr)
print('OK.')
