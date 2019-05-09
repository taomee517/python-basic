import turtle
import math

x0,y0 = 0,0
x1,y1 = 0,200
x2,y2 = 200,0
x,y = 103,103

# 绘制三角形
turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x0,y0)

# 计算斜边长度
distance = math.sqrt((y1-y0)**2 + (x2-x1)**2)

# 标记斜边长度
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("red")
turtle.write(distance)
turtle.done()