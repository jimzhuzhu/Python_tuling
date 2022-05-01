import time
import datetime

# datetime.date
dt = datetime.date(2020, 5, 24)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time
dtt = datetime.time(22, 40, 12, 6)
print(dtt)
print(dtt.hour)
print(dtt.minute)
print(dtt.second)
print(dtt.microsecond)

# datetime.datetime
from datetime import datetime,timedelta
dt = datetime(2020, 5, 24)
print(dt.today())
print(dt.now())
print(dt.utcnow())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H;%M:%S"))