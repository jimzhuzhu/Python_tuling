# 变量可以赋值
a = 100
b = a

# 函数名称就是一个变量
def funA():
    print("funA")

funB = funA
funB()

# 返回一个传入100倍的数字
def funA(n):
    return n * 100
# 再写一个函数，把传入参数乘以300倍
def funB(n):
    # 最终是想返回300n
    return funA(n) * 3
print(funB(9))

# 写一个高阶函数
def funC(n, f):
    # 假定函数是把n扩大100倍
    return f(n) * 3

print(funC(9, funA))

# 比较funC 和funB, x显然funC的写法更优于funB
# 举例：
def funD(n):
    return n * 10
# 需求变更，把n放大三十倍，此时funB则无法实现
print(funC(6, funD))