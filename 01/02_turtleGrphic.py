import turtle
t = turtle.Turtle("turtle")
t.forward(100)
t.left(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.fd(100)

#펜컬러 설정
t.pencolor('red')
t.circle(100)

t.pencolor("blue")
t.rt(360/3)
t.fd(100)
t.lt(360/3)
t.fd(100)
t.lt(360/3)
t.fd(100)

turtle.done()
turtle.exitonclick()