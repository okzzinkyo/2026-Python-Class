import turtle

t=turtle.Turtle()
t.width(5)

colorList = ['red', 'orange', 'green', 'blue', 'purple']
for n in range(18):
    t.left(20)
    t.color(colorList[n%5])
    for i in range(4):
        t.forward(100)
        t.left(90)
        
turtle.done()