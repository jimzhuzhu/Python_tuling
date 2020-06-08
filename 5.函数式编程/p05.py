# filter
# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
# 对于一个列表。对其进行过滤，偶数组成一个新的列表
def isEven(a):
    return a % 2 == 0
l = [1,2,3,4,5,6,7,8,9,10]
rst = filter(isEven, l)
# 返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)

print([i for i in rst])
