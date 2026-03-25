import math

a = float(input("2차 방정식의 계수 a를 입력하세요."))
b = float(input("2차 방정식의 계수 b를 입력하세요."))
c = float(input("2차 방정식의 계수 c를 입력하세요."))

if a == 0 :
    print('a=0, 근은 -c/b')
    print("x=", -c/b)
else :
    discriminant = b**2 - 4*a*c
    if discriminant == 0 :
        print("D=0, 두 근이 일치하는 중근을 가진다.")
        print("x=", -b/(2*a))
    elif discriminant > 0 :
        print("D>0, 서로 다른 두 실근을 가진다.")
        print("x1=", (-b + math.sqrt(discriminant))/(2*a))
        print("x2=", (-b - math.sqrt(discriminant))/(2*a))
    else :
        print("D<0, 실근이 존재하지 않는다.")