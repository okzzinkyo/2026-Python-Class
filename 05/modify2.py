def modify2(li):
    li += [100,200]

list = [1,2,3,4,5]

print(list) # [1,2,3,4,5]

modify2(list)

print(list) # [1,2,3,4,5,100,200]
# 값을 매개변수로 전달하는 경우와 달리 list는 참조 주소를 매개변수로 전달
# list는 변경 가능한 객체(mutable object)이기 때문에 +=로 추가하면 전역에 선언된 list가 변경됨