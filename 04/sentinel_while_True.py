n = 0
total = 0

while True:
    score = int(input("성적을 입력하시오:"))
    if(score < 0):
        break
    total += score
    n+=1

if n == 0 :
    print("입력된 성적이 없습니다.")
elif(n > 0):
    avg = total/n
    print("성적의 평균은 %f점 입니다" %avg)