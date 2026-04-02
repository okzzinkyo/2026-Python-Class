input_text = input("문자열을 입력하세요: ")

alphabet_count = 0
digit_count = 0
space_count = 0

for char in input_text:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1

print("알파벳 개수: ", alphabet_count)
print("숫자 개수: ", digit_count)
print("공백 개수: ", space_count)