# map
# 有一个列表，想对列表里的每一个元素乘10，并得到新的列表

l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

# 利用map映射实现
def mulTen(n):
    return n * 10

l3 = map(mulTen,l1)
# map类型是一个可迭代的结构，所以可以使用for遍历打印出来
for i in l3:
    print(i)

# 以下列表为何为空
l4 = [i for i in l3]
print(l4)