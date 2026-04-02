import turtle
t = turtle.Turtle("turtle")
t.shape("turtle")
t.speed(0)
t.pensize(3)
t.pencolor("red")
t.penup()
t.goto(0,0)
t.pendown()

user_input = ""
while user_input != "quit":
    user_input = input("명령어를 입력하시오: (left,right,forw,back,quit): ")
    if user_input == "left":
        t.left(90)
    elif user_input == "right":
        t.right(90)
    elif user_input == "forw":
        t.forward(100)
    elif user_input == "back":
        t.backward(100)
    elif user_input == "quit":
        break
    else:
        print("잘못된 명령어입니다.")

turtle.done()