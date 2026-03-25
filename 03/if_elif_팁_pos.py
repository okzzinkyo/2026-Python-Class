price = int(input("음식 값은? $"))
inputTip= int(input("팁을 선택하세요:\n1.10%\n2.15%\n3.20%\n팁 선택(1\\2\\3):"))


if inputTip == 1 :
    tipPercent = 0.10
elif inputTip == 2:
    tipPercent = 0.15
elif inputTip == 3:
    tipPercent = 0.20
else : 
    print("올바른 선택이 아닙니다. 기본값인 15%로 계산합니다.")
    tipPercent = 0.15

print(f'음식 값:${price:.2f}')
print(f'선택한 팁:{tipPercent*100}%')
print(f'팁 금액:${price*tipPercent}')
print(f'총 지불 금액:${price + price*tipPercent}')
