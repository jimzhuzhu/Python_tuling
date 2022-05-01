import time
# 把时间表示自己想要显示的格式
# 遇到中文格式使用format进行格式内容
t = time.localtime()
ft = time.strftime("%Y{}%m{}%d{} %H:%M", t).format("年", "月", "日")
print(ft)