import turtle
import time
t = turtle.Pen()
t.pensize(5)
t.speed(10)
#画哆啦A梦
def my_circle(x,y,color,size):
    t.setheading(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(size)
    t.end_fill()

def simle():
    #t.forward(10)
    t.up()
    t.goto(-80,100)
    t.down()
    t.right(90)
    t.circle(80,180)


def myline(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

my_circle(0,0,(0.1,0.5,1),180)#大脸
my_circle(0,0,"white",130)#小脸
my_circle(-60,160,"white",60)#左大眼睛
my_circle(60,160,"white",60)#右大眼睛
my_circle(-40,190,"black",20)#左小眼睛
my_circle(-40,200,"white",8)#左小白点
my_circle(40,190,"black",20)#右小眼睛
my_circle(40,200,"white",8)#左小白点
my_circle(0,120,"red",30)#鼻子
my_circle(-10,150,"white",6)#鼻子小白点

#右边胡子
myline(50,70,130,35)
myline(50,100,120,100)
myline(50,130,130,160)
#左边胡子
myline(-50,70,-130,35)
myline(-50,100,-120,100)
myline(-50,130,-130,160)
#装饰
myline(0,120,0,20)
simle()

#画爱心
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

#心里面显示的文字
maxim= "null==undefined"
maxim2="Never Say Never"
maxim3="May the force be with you"

#谁制作
me = "By Simon"
# 窗口大小
turtle.setup(width=900, height=500)
# 颜色
turtle.color('pink')
# 笔粗细
turtle.pensize(3)
# 速度
turtle.speed(50)
# 提笔
turtle.up()
# 隐藏笔
turtle.hideturtle()
# 去到的坐标,窗口中心为0,0
turtle.goto(0, -300)
turtle.showturtle()
# 画上线
turtle.down()
turtle.speed(20)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
# 调用画爱心左边的顶部
LittleHeart()
# 调用画爱右边的顶部
turtle.left(120)
LittleHeart()
# 画下线
turtle.forward(224)
turtle.end_fill()
turtle.pensize(30)
turtle.up()
turtle.hideturtle()
# 在心中写字 一次
turtle.goto(0, -200)
turtle.showturtle()
turtle.color('white', 'pink')
# 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
turtle.write(maxim, font=('gungsuh', 10,), align="center")
turtle.up()
turtle.hideturtle()
time.sleep(2)
# 在心中写字 二次
turtle.goto(0, -150)
turtle.showturtle()
turtle.color('yellow', 'pink')
turtle.write(maxim2, font=('gungsuh', 20,), align="center")
turtle.up()
turtle.hideturtle()
time.sleep(2)
# 在心中写字 三次
turtle.goto(0, -100)
turtle.showturtle()
turtle.color('red', 'pink')
turtle.write(maxim3, font=('gungsuh', 25,), align="center")
turtle.up()
turtle.hideturtle()
# 写署名
if me != '':
    turtle.color('black', 'pink')
    time.sleep(2)
    turtle.goto(180, -300)
    turtle.showturtle()
    turtle.write(me, font=('宋体',20,), align="center", move=True)

content = []
for y in range(30,-30,-1):
        for x in range(-30,30):
                subcontent = []
                if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0:
                        subcontent.append('Simon'[(x-y)%4])
                else:
                        subcontent.append(' ')
                content.append(''.join(subcontent))
        content.append('\n')
print(''.join(content))
# 点击窗口关闭
window = turtle.Screen()
window.exitonclick()

