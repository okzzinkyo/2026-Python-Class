#print함수를 이용하여 변수와 텍스트를 동시 출력
x = 20
print(f"결과: x")
print("결과: x")
print(f"결과: {x}")
print("결과:",x)
print("결과:"+str(x))
print("결과: %d" %x)

#오류 - 문자열 + 정수 이기 때문에
print("결과:" + x)