def func_1(x,y):
    print("함수가 실행됨", x+y)

def func_2():
    print("매개변수가 필요 없는 함수")

func_1(2,10)
func_2()

v = func_1(2,10)
print(type(v))

n=''
print(type(n))


def func_3(x,y):
    return(x+y)

x= func_3(10,20)
y= func_1(10,20)

print(x,y)