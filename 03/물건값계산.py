amount = int(input("구입 금액을 입력하시오."))
if amount >=100000:
    amount = amount*0.95

print(f"지불금액은 {amount}입니다.")