from random import randint

tries = 0
answer = randint(1, 100)
print("1부터 100 사이의 숫자를 맞추시오")
while tries < 10:
    g = int(input("숫자를 입력하시오:"))
    tries += 1
    if answer > g :
        print("up")
    elif answer < g :
        print("down")
    else:
        break

if answer == g:
    print("정답! 시도 횟수는 %d번입니다." % tries)
else:
    print("실패! 횟수를 초과했습니다. 정답은 %d입니다." % answer)