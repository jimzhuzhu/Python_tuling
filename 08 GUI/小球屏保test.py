import random
import tkinter


class Ball(object):
    """定义运动球的类"""
    def __init__(self, canvas, scrnwidth, scrnheight):
        """
        实例化一个画布，
        定义屏幕的宽高
        随机球的运动方向和运动速度，
        随机球的大小半径，
        随机球的颜色 rgb
        """
        self.canvas = canvas
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        self.xpos = random.randint(20, scrnwidth-20)
        self.ypos = random.randint(20, scrnheight-20)

        self.xv = random.randint(2, 20)
        self.yv = random.randint(2, 20)

        self.radius = random.randint(10, 50)

        col = lambda:random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (col(), col(), col())

    def create_ball(self):
        """用构造函数定义的变量值，在canvas上画一个球"""
        # 通过四个坐标画椭圆
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2,
                                            fill=self.color,
                                            outline=self.color)

    def move_ball(self):
        """在画布上挪动图画，要先有球
        移动球的时候，要控制球的方向，每次移动球有一个新的坐标"""
        self.xpos = self.xpos + self.xv
        self.ypos += self.yv

        if self.xpos >= self.scrnwidth - self.radius:
            self.xv = -self.xv
        if self.ypos >= self.scrnheight - self.radius:
            self.yv = -self.yv
        if self.xpos <= self.radius:
            self.xv = abs(self.xv)
        if self.ypos <= self.radius:
            self.yv = abs(self.yv)

        self.canvas.move(self.item, self.xv, self.yv)


class ScreenSaver(object):
    """定义屏保的类，可以被启动"""

    # 用列表装随机产生的球
    balls = list()
    def __init__(self):
        """每次启动小球数量随机
        利用tkinter上制作GUI框
        GUI没有边框
        任何移动鼠标或键盘退出GUI
        创建一个画布，画布大小根据电脑宽高设置
        在画布上利用列表画球,
        屏保自己启动
        """
        self.num_balls = random.randint(6,20)

        self.root = tkinter.Tk()
        self.root.overrideredirect()
        self.root.wm_title('小球屏保')
        self.root.bind('<Motion>', self.myquit)
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()


        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        for i in range(self.num_balls):
            ball = Ball(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()

        self.root.mainloop()

    def run_screen_saver(self):
        """让每个球都调用move_ball使球移动功能函数
        利用after实现球每隔一段时间调用函数继续移动"""
        for ball in self.balls:
            ball.move_ball()

        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, event):
        """销毁函数，把创建的GUI撤销掉
        只是利用了事件处理机制
        实际上并不关心事件的类型"""
        self.root.destroy()


if __name__ == '__main__':
    # 启动屏保
    ScreenSaver()