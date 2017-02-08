import json

a = '{"empty": false}'
teststr = json.loads(a)
print teststr
print teststr['empty']