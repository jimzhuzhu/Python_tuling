# 简单异常案例
# 给出提示信息
try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是： {0}".format(rst))
# 捕获异常后，把异常实例化，出错信息就会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisonError异常并实例化实例e
except ZeroDivisionError as e:
    print("你输入的什么玩意，0不能作为分母")
    print(e)
    # exit是退出程序的意思
    exit()

# 思考： 为什么可以直接打印实例e,此刻实例e应该实现了哪个函数