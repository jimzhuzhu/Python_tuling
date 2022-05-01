import calendar

# monthrange
# w代表这个月周几开始
# t代表共多少天
w,t = calendar.monthrange(2020,5)
print(w)
print(t)

# monthcalendar
# 返回一个月每天的矩阵列表
m = calendar.monthcalendar(2020, 5)
print(type(m))
print(m)

# prcal:
# 直接打印日历
calendar.prcal(2020)

# prmonth
# 直接打印月日历

calendar.prmonth(2020,5)

# weekday()
# 获取周几
print(calendar.weekday(2020, 5, 21))