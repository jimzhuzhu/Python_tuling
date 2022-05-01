import time
# 当前时区与标准UTC相差秒数
print(time.altzone)

# 测当前是否是夏令时
print(time.daylight)

#得到时间戳
t = time.time()
print(t)

# 得到当前时间的时间结构
t = time.localtime()
print(t)
print(t.tm_hour)

# asctime 返回元组的正常字符串格式化之后的时间结构
tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime 获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime 使用时间元组获取对应的时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

# clock
def p():
    time.sleep(2.5)

t0 = time.clock()
# p()
t1 = time.clock

# sleep 使程序睡眠，n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)