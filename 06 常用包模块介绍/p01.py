# calendar 导入
import calendar
# claendar: 获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符串
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2020)
# 打印类型
print(type(cal))
# 打印2020日历字符串
print(cal)

cal = calendar.calendar(2020, w=2, l=0, c=3)
print(cal)

print(calendar.isleap(2020))
