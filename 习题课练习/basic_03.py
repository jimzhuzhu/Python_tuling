# 等价表达式 判断是否相等
cost = input("请输入你的数字")
cost= int(cost)
print(type(cost))
if 10 < cost < 50:
    print(True)
else:
    print(False)

if (10 < cost) and (cost < 50):
    print(True)
else:
    print(False)

# 使用int()将小数转换为整数，结果是向上取整还是向下取整
print(int(3.4))
# 向下取整

# 写一个程序