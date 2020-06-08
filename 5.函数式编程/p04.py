from functools import reduce

# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
# 对于；列表执行myAdd的reduce操作
rst = reduce(myAdd, [1,2,3,4,5,6,7,8,9,10])
print(rst)