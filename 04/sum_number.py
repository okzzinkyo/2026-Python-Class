sum=0

start_number = int(input("어디부터 계산할까요:"))
end= int(input("어디까지 계산할까요:"))
increase_by = int(input("숫자를 얼마만큼 증가시킬까요?:"))

for x in range(start_number, end+1, increase_by):
    sum+=x

print(start_number,"부터",end,"까지의 정수의 합=",sum)