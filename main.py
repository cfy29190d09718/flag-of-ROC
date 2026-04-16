#此程序目的为绘制中华民国（台湾ROC）国旗，编写语言为python，使用turtle库进行编写
#本国旗根据比例、颜色等参数均根据《中华民国宪法》《中华民国国徽国旗法》绘制，具体参数来自维基百科（https://en.wikipedia.org/wiki/Flag_of_the_Republic_of_China）
#绘制的精细度有细微偏差：1十二金光光芒处不应有连接  2：十二金光光芒底部要有弧度
#目前程序比较屎山，可以创建def,class,绘图方面可以用math库改进

import turtle
#import math

a = 6.5       #等比例放大、缩小
listx = list()      #十二金光尖尖处x轴坐标
listy = list()      #十二金光尖尖处y轴坐标
listxx = list()     #十二金光底部x轴坐标
listyy = list()     #十二金光底部y轴坐标

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800,600)       #窗口大小可更改
screen.colormode(255)

#————绘制红色底色————
t.penup()
t.goto(-60*a,-40*a)
t.pendown()
t.pencolor(243,0,1)
t.color(243,0,1)
t.begin_fill()
t.goto(60*a,-40*a)
t.goto(60*a,40*a)
t.goto(-60*a,40*a)
t.goto(-60*a,-40*a)
t.end_fill()

#————绘制左上角青蓝色部分————
t.pencolor(0,40,204)
t.penup()
t.goto(-60*a,40*a);
t.pendown()
t.color(0,40,204)
t.begin_fill()
t.goto(-60*a,0)
t.goto(0,0)
t.goto(0,40*a)
t.goto(-60*a,40*a)
t.end_fill()

#————绘制太阳圆————
t.pencolor(255,255,255)
t.penup()
t.goto(-30*a,(20-7.5)*a)
t.pendown()
t.color(255,255,255)
t.begin_fill()
t.circle(7.5*a)
t.end_fill()

#————绘制十二金光————
t.penup()
t.goto(-30*a,20*a)
t.pencolor(0,0,0)
t.color(255,255,255)
for i in range(0,12):       #计算十二金光尖尖处坐标，存入列表
    t.forward(15*a)
    listx.append(t.xcor())
    listy.append(t.ycor())
    t.goto(-30*a,20*a)
    t.left(30)
t.right(15)     #右转15°，计算十二金光底部坐标
for i in range(0,15):       #计算十二金光底部坐标，存入列表（循环范围应大于13，便于绘画时读取列表数据）
    t.forward(8.5*a)
    listxx.append(t.xcor())
    listyy.append(t.ycor())
    t.goto(-30*a,20*a)
    t.left(30)
t.penup()
for i in range(12):     #画十二金光
    t.goto(listx[i],listy[i])
    t.pendown()
    t.begin_fill()
    t.goto(listxx[i],listyy[i])
    t.goto(listxx[i+1],listyy[i+1])
    t.goto(listx[i],listy[i])
    t.end_fill()
    t.penup()

#————数据调试区————
for i in range(0,13):
    print(listxx[i]," ",listyy[i],"\n")

turtle.done()

