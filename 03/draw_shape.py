import turtle
t=turtle.Turtle()
shape = input("어떤 도형을 그리시겠습니까?(원/사각형/삼각형):")

if shape == '원':
    radius = float(input("반지름을 입력하세요:"))
    t.circle(radius)
elif shape == '사각형':
    l1 = float(input("가로 변의 길이를 입력하세요."))
    l2 = float(input("세로 변의 길이를 입력하세요."))

    # t.forward(l1)
    # t.left(90)
    # t.fd(l2)
    # t.left(90)
    # t.fd(l1)
    # t.left(90)
    # t.fd(l2)

    # 반복문 활용
    for i in range(2):
        t.forward(l1)
        t.left(90)
        t.fd(l2)
        t.left(90)
        
elif shape == '삼각형':
    l1 = float(input("한 변의 길이를 입력하세요."))

    for i in range(3):
        t.forward(l1)
        t.left(120)

else :
    print("지원하지 않는 도형입니다.")

t.done();