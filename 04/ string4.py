input_text = input("문자열을 입력하세요: ")
word = input_text.lower()

if  len(input_text) and input_text.isalpha():
    for index, char in enumerate(word):
        if char in "aeiou":
            print(f"모음 '{char}'가 {index}번째 위치에 있습니다.", end="\n")