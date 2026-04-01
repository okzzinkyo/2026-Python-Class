keyword_list = []
input_word = ''

while True:
    input_word = input("단어를 입력하세요 ('quit'으로 종료):")
    if(input_word == 'quit'):
        break
    keyword_list.append(input_word)

print("입력된 단어 개수: %d" %len(keyword_list))
print("입력된 단어 목록:", list(keyword_list))