# 简单异常案例
# 给出提示信息
try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是： {0}".format(rst))
# 如果是多个error的情况
# 需要把越具体的错误，放在前面
# 在异常类继承关系中，越是子类的异常，越要往前放
# 越是父类的异常，越往后放

# 在处理异常的时候，一旦拦截到某一个异常，就不会继续往下查看，直接进入下一个
# 代码，即有finally则执行这个语句块，否则执行下一个大的语句
except ZeroDivisionError as e:
    print("你输入的什么玩意，0不能作为分母")
    print(e)
    # exit是退出程序的意思
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print(e)
    exit()
# 所有异常都是继承自Exception
# 如果写上下面的这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个exception
except Exception as e:
    print("我也不知道哪里错啦")
    print(e)
    exit()
print("hahahahaha")
