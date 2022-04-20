import math
import keyword
import random
# 查看系统保留的关键字，不可以用来当作变量命名
print(keyword.kwlist)
# print(math)
# ceil()向上取整操作
print(math.ceil(5.9))
print(math.ceil(5.001))

print('='*20)
# floor() 向下取整操作
print(math.floor(5.9))
print(math.floor(5.001))

print('='*20)
# round() 四舍五入操作,不是math里面的内置函数，是系统的函数，直接给值
print(round(5.4))
print(round(5.5))

print('='*20)
# sqrt() 开平方操作 返回浮点数
print(math.sqrt(4))
# sin() 正弦函数
print(math.sin(0.5))

print('='*20)
# pow() 与幂运算差不多，计算一个数的几次方，返回浮点数
# 两个参数，第一个是底数，第二个是指数
print(math.pow(4, 3))
# 等于4的3次方，幂运算，返回整形
print(4**3)

print('='*20)
# fabs() 对一个数获取绝对值,返回浮点数
print(math.fabs(-4))
print(math.fabs(3))
print(math.fabs(0))

# abd() 获取绝对值操作，返回值由本身类型而定，不是数学模块中，python内置
print(abs(-4))
print(abs(-4.5))

print('='*20)
# fsum() 对整个序列求和,返回浮点数
a = 1, 2, 3, 4, 5, 6
print(math.fsum(a))
# sum() 求和，python内置
a = 1, 2, 3, 4, 5, 6
print(sum(a))

print('='*20)
# math.modf(),把数字拆解成小数部分和整数浮点数，组成一个元组，小数在前，整数部分在后
print(math.modf(4.5))
print(math.modf(99))

print('='*20)
# copysign() 将第二个的符号(正负号)传给第一个数
# 返回带符号的第一个数值，且是浮点数
print(math.copysign(2, -4))

print('='*20)
# 打印自然数e和 π的值
print(math.e)
print(math.pi)

print('='*20)
# random(）获取0-1之间的随机小数，包含0不包含1
# randint() 随机取序列中的数值，包含起始和结束
for i in range(10):
    print(random.random(), end='|')
    print(random.randint(1, 10))

# randrange() 获取指定开始和结束之间的值，可以指定间隔值
# 包含起始不包含结束
for i in range(5):
    print(random.randrange(1, 9, 3))

print('='*20)
# choice() 随机获取列表中的值
a = [1, 2, 3, 4, 5, 6, 7]
b = random.choice(a)
print(b)

print('='*20)
# shuffle 随机打乱列表,返回值是None
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)

print('='*20)
# uniform() 随机获取指定范围内的值，包括小数
print(random.uniform(1, 4))
