score = 0

answer = input('가장 쉬운 프로그래밍 언어는?')
result = answer == '파이썬'
score += int(result)

answer = input('거듭제곱을 계산하는 연산자는?')
result = answer == '**'
score += int(result)

answer = input('파이썬에서 출력시에 사용하는 함수이름은?')
result = answer == 'print'
score += int(result)

print('점수 =', score)