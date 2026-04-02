x = int(input("첫 번째 숫자를 입력하시오(큰수): "))
y = int(input("두 번째 숫자를 입력하시오(작은수): "))

while y != 0:
    if y == 0:
        print("최대 공약수는",x,"입니다.")
        break
    r = x % y
    x,y = y,r

print("최대 공약수는",x,"입니다.")