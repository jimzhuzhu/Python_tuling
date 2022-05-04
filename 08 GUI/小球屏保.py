# 需求分析
# 1. 随机或者指定个数的球
# 2. 球颜色，大小，运动速度，放心都随机
# 3. 监听鼠标动作，有动作就退出
# 4. 应该没有边框

# 构成： 1.球， 2. 世界

import tkinter
import random


class Ball(object):
    """
    定义运动球的类
    """
    def __init__(self, canvas, screenwidth, screenheight):
        """canvas：画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        screenwidth/screenheight：屏幕宽高
        """
        # 实例化一个画布
        self.canvas = canvas
        # 定义球的颜色，此处用lambda表达式
        #  颜色- rgb（0-255）
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

        # 球的大小随机，此处球的大小用半径表示
        self.radius = random.randint(10, 50)

        # 球出现的初始位置要随机，此处位置表示球的圆心
        # x_pos 表示x的坐标， y_pos 表示y的坐标
        self.x_pos = random.randint(20, screenwidth-20)
        self.y_pos = random.randint(20, screenheight-20)

        # 定义球的运动速度
        # 模拟运动，不断擦掉原来的画，然后在新的地方绘制
        # 此处代表球在x和y轴的方向运动
        self.xv = random.randint(2, 20)
        self.yv = random.randint(2, 20)

        # 定义屏幕的宽和高
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    def create_ball(self):
        """用构造函数定义的变量值，在canvas上画一个球"""

        # tkinter 没有画圆函数，只有oval画椭圆函数，画椭圆需要定义两个坐标
        # 求两个坐标的方法：已知圆心的坐标，则圆心坐标减去半径能求出左上角，加上可以求出右下角坐标
        x1 = self.x_pos - self.radius
        y1 = self.y_pos - self.radius

        x2 = self.x_pos + self.radius
        y2 = self.y_pos + self.radius

        # 在有两个对角坐标的前提下，可以进行画椭圆
        # fill代表填充颜色，outline代表外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2,
                                            fill=self.color,
                                            outline=self.color)

    def move_ball(self):
        """
        移动球的时候，要控制球的方向，每次移动球有一个新的坐标
        """
        self.x_pos += self.xv
        self.y_pos += self.yv

        # 判断是否会撞墙，撞了后就要随机回头
        if self.x_pos >= self.screenwidth - self.radius:
            self.xv = -self.xv
        if self.x_pos <= self.radius:
            self.xv = abs(self.xv)
        if self.y_pos >= self.screenheight - self.radius:
            self.yv = -self.yv
        if self.y_pos <= self.radius:
            self.yv = abs(self.yv)

        self.canvas.move(self.item, self.xv, self.yv)


class SS:
    """定义屏保的类，可以被启动"""

    # 建一个列表，用于装随机产生的球
    balls = []

    def __init__(self):
        """每次启动球的数量随机，取消边框，得到屏幕规格，创建画布"""
        self.num_balls = random.randint(6, 20)

        # 创建GUI主屏幕
        self.root = tkinter.Tk()
        # 设置标题名
        # 取消边框设置
        self.root.wm_overrideredirect()
        # 调整背景透明度
        self.root.wm_attributes('-alpha', 9)
        # 移动鼠标，点击鼠标，敲击键盘时退出屏保
        self.root.bind('<Motion>', self.my_quit)
        self.root.bind('<Any-Button>', self.my_quit)
        self.root.bind('<Key>', self.my_quit)
        # 得到屏幕的宽窄信息，作为主窗口尺寸
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 创建画布，包括画布的归属和规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球，调用类Ball和函数create_ball
        for i in range(self.num_balls):
            ball = Ball(self.canvas, screenwidth=w, screenheight=h)
            ball.create_ball()
            # 把球元素添加到列表里
            self.balls.append(ball)
        # 调用运动球的函数
        self.run_screen_saver()
        # 进入主循环
        self.root.mainloop()

    def run_screen_saver(self):
        """遍历列表balls，使每个球进行移动"""
        for b in self.balls:
            b.move_ball()
        # after是200毫秒启动一次函数，需要启动的函数是第二个参数
        self.canvas.after(200, self.run_screen_saver)

    def my_quit(self, event):
        """此处只关心利用了事件处理机制，不关心事件的类型"""
        self.root.destroy()


if __name__ == '__main__':
    # 调用类SS，启动屏保
    SS()
