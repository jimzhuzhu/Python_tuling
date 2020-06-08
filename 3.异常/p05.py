# raise 案例
# 也可以自己定义异常名
# 需要注意:自定义异常必须是系统异常的子类.继承

class ZhuValueError(ValueError):
    pass
try:
    print("我爱刘雨霞")
    print("真的哦")
    # 手动引发一个异常
    # 注意语法： raise ErrorClassName (异常类）
    raise ZhuValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
except ZhuError as e:
    print("ZhuValueError")
except Exception as e:
    print("有异常")
finally:
    print("无论怎么样，我肯定会被执行的")