input_text = input("문자열을 입력하세요: ")
word = input_text.lower()

vowel_count = 0
consonant_count = 0

if  len(input_text) and input_text.isalpha():
    for char in word:
        if char in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

print("모음 개수: ", vowel_count)
print("자음 개수: ", consonant_count)