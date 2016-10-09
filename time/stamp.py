import time
import datetime

a1 = '2016-05-23 18:42:39.016789'

def getTime(dateStr):
    b = datetime.datetime.strptime(a1, '%Y-%m-%d %H:%M:%S.%f')
    return int(time.mktime(b.timetuple()) * 1000) + int(b.microsecond / 1000)

print(getTime(a1))
