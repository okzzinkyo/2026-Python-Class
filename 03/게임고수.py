level = int(input("현재 레벨을 입력해 주세요:"))
exp = int(input("현재 경험치를 입력해 주세요:"))

if(level>=10 and exp >=500):
    title =  "고수"
else :
    title = "초보"

print(f"당신은 {title}입니다.")