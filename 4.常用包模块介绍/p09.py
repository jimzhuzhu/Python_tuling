import time
import timeit

# timeit 测量函数执行时间
def doIt():
    num = 3
    for i in range(num):
        print("Repaet for {0}".format(i))
# 执行函数，重复10次
t = timeit.timeit(stmt=doIt, number=10)
print(t)

s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
# 执行doIt(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创建了一个小环境
# 在创作的小环境中，代码执行的顺序大致是
#
'''
def doIt(num):
    ....
num = 3
doIt(num)
'''
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)
print(t)