#반복을 이용한 팩토리얼 구하기

fact =1
n = int(input("정수를 입력하시오:"))

if n <=0:
    print("음수와 0은 팩토리얼을 구할 수 없습니다.")
else :
    for i in range(1,n+1):
        fact = fact*i
    print(f"{n}!은 {fact}이다.")