# sorted排序
a = [2,5,1,76,8,23,7,21,874,10,8]
# 默认是正序
al = sorted(a)
print(al)
# reverse=True倒序
al2 = sorted(a, reverse=True)
print(al2)

# 案例2
a = [24,-22,56,23,-5,7,10,-99]
# 按照绝对值进行排序
# abs是求绝对值的意思
# 即按照绝对值倒叙排序
al3 = sorted(a, key=abs, reverse=True)
print(al3)

# 案例3
astr = ["zhuzhu", "xiaoliu", "zhuxianfu", "Liu yu xia"]
str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.title)
print(str2)