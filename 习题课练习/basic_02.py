# Python 中提供了 68个BIF内建函数

# ”Tuling" 和 "tuling" 是不一样的

# "=" 等号是用来复制的
# " == " 是用来判断两个对象是否相等

# 字符串的拼接
a = "我喜欢" + "liuxiaoxia" + ", 他也很喜欢我"
print(a)

# 编写程序，要求用户输入姓名并打印”你好，姓名“

name = input("请输入你的姓名")
print("Hello," + name)

# 判断数字,需要先判断是否输入的是数字，然后进行类型转化

number = input("请输入1-100之间的整数")
if number.isdigit():
    number = int(number)
    if 1 <= number <= 100:
        print("你真棒")
    else:
        print("你的数学是体育老师教的吗？")
else:
    print("你是傻呀，你输的是数字吗？")