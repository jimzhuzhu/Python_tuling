import random

# random()
print(random.random())

# randint(a,b) 返回a到b的随机整数，包含a，b
# 随机生成0-100的整数
print(random.random(0,100))

# choice() 随机挑选
l = [str(i)+"haha" for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)

# shuffle 随机打乱列表
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)