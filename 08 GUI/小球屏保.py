# 需求分析
# 1. 随机或者指定个数的球
# 2. 球颜色，大小，运动速度，放心都随机
# 3. 监听鼠标动作，有动作就退出
# 4. 应该没有边框

# 构成： 1.球， 2. 世界

import tkinter
import random


class Ball(object):
    def __init__(self, canvas, screenwidth, screenheight):
        self.canvas = canvas

        # 2.球颜色，大小，运动速度和方向随机
        #  颜色- rgb（0-255）
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x'%(c(), c(), c())

        self.radius = random.randint(40, 120)

        self.xpos = random.randint(20, screenwidth-20)
        self.ypos = random.randint(20, screenheight-20)

        self.xv = random.randint(5, 50)
        self.yv = random.randint(5, 50)

        self.scrnwidth = screenwidth
        self.scrnheight = screenheight

    def create_ball(self):
        """画布上画一个球"""
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius

        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2,
                                            fill=self.color,
                                            outline=self.color)


if __name__ == '__main__':

    root = tkinter.Tk()
    root.wm_title('小球屏保')
    can = tkinter.Canvas(root, width=200, height=200)
    can.pack()
    b = Ball(can, screenwidth=150, screenheight=150)
    b.create_ball()
    root.mainloop()
