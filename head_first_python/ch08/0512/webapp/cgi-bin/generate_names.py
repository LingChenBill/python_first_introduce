#! /usr/bin/env python
# Date:2020/5/12
# Author:Lingchen
# Mark: 将数据作为一个Json数据流返回给Web请求者
import json
import athletemodel
import yate

names = athletemodel.get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))
