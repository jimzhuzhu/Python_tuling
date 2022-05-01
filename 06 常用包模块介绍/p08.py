import time
import timeit

# timeit 时间测量工具
def p():
    time.sleep(3.6)

t1 = time.time()
p()
print(time.time() - t1)


# 程序运行速度案例
# 如果单纯比较生存一个列表的时间，很难判断实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
# 测量代码c执行10000次运行结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)
