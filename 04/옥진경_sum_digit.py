number = 1234
digit_sum = 0

while number > 0 :
    digit = number % 10
    digit_sum += digit
    number = number//10

print(f"자리수의 합은 {digit_sum}입니다.")