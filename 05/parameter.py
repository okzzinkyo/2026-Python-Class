def sub(mylist):
    mylist = [1,2,3,4] # 새로운 리스트가 매개 변수로 할당 됨
    print("함수 내부에서의 mylist:",mylist) 
    return

mylist = [10,20,30,40]
sub(mylist)
print("함수 외부에서의 mylist:",mylist)