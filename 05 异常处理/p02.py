# 简单异常案例
try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是： {0}".format(rst))
except:
    print("你输入的什么玩意，0不能作为分母")
    # exit是退出程序的意思
    exit()