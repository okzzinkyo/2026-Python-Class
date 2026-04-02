import turtle
t = turtle.Turtle("turtle")
t.speed(0) # 거북이 속도 최대
colors = ["red","orange","yellow","green","blue","purple"]

for color in colors:
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.right(60)
turtle.done()