# 以lambda开头，紧跟一定参数(如果有参数)
# 参数后面用冒号和表达式主题隔开
# 只是一个表达式，没有return

# 计算一个数字的100倍数
# 因为是一个表达式，所以没有return
stm = lambda x: 100 * x
print(stm(89))

stm2 = lambda x, y, z: x + y*10 + z*100
print(stm2(1,2,3))