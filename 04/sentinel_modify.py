n = 0
total = 0
score = 0

print("종료하려면 음수를 입력하시오")
while score >= 0:
    score = int(input("성적을 입력하시오:"))
    if(score > 0) :
        total = total + score
    n += 1

if n ==1 :
    print("입력된 성적이 없습니다.")
elif(n > 1):
    avg = total/(n-1)
    print("성적의 평균은 %f점 입니다" %avg)