# else 语句案例

try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是： {0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("无论如何我都会被执行")