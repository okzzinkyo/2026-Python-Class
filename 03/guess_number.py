from random import randint

isAnswer = False
answer = randint(1, 100)
print("숫자 게임에 오신 것을 환영합니다.")
while not isAnswer:
    g = int(input("숫자를 맞춰보세요."))
    if answer > g :
        print("up")
    elif answer < g :
        print("down")
    elif answer == g :
        print("정답")
        isAnswer = True

