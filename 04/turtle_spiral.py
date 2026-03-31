import turtle

# window = turtle.Screen()
# window.bgcolor("pink")
turtle.bgcolor("pink")

t=turtle.Turtle("turtle")
t.color("blue")

size = 20
for x in range(30):
    t.stamp()
    size = size+3
    t.forward(size)
    t.right(24)

turtle.done()