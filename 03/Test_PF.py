engScore = float(input("영어 점수 입력:"))
mathScore = float(input("수학 점수 입력:"))
total = mathScore + engScore

if mathScore >= 40 and engScore >= 40 and total > 110 :
    print("합격입니다.")
elif mathScore < 40 and engScore < 40:
        print("불합격: 수학과 영어 점수가 부족합니다.")
else :
    if mathScore < 40:
        print("불합격: 수학 점수가 부족합니다.")
    elif engScore < 40:
        print("불합격: 영어 점수가 부족합니다.")
    else :
        print("불합격: 총합 점수가 부족합니다.")