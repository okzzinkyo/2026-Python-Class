def printOption():
    print("'c' 섭씨 온도에서 화씨온도로 변환")
    print("'f' 화씨온도에서 섭씨온도로 변환")
    print("'q' 종료")
    option = input("메뉴에서 선택하세요.")
    return option

def FtoC():
    temp_f = float(input("섭씨온도:"))
    temp_c = (temp_f-32.0) * 5/9
    return temp_c

def CtoF():
    temp_c = float(input("화씨온도:"))
    temp_f = 9 / 5 * temp_c + 32.0
    return temp_f

# option = ''
# while (option != 'q'):
#     option = printOption()
#     if option == 'c' :
#         print('화씨온도', CtoF())
#     elif option == 'f' :
#         print('화씨온도', FtoC())

while True :
    option = printOption()
    if(option == 'q'):
        break
    elif option == 'c':
        print('화씨온도', CtoF())
    elif option == 'f':
        print('화씨온도', FtoC())