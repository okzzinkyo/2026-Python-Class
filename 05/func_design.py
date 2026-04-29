def readList():
    nlist = []
    flag = True
    while flag:
        number = int(input("숫자를 입력하시오: "))
        if number < 0:
            flag = False
        else :
            nlist.append(number)

    return nlist

def processList(nlist):
    nlist.sort()
    return nlist

def printList(nlist):
    for i in nlist:
        print("성적=", i)


# 모듈 사용
# import func_design
# func_design.readList()
# 숫자를 입력하시오: 100
# 숫자를 입력하시오: 50
# 숫자를 입력하시오: -1
# [100, 50]
# func_design.processList(['a','b','c','x','d'])
# ['a', 'b', 'c', 'd', 'x']
# func_design.printList([100,50])
# 성적= 100
# 성적= 50