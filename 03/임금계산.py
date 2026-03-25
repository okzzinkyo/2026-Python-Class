time = int(input("근무시간을 입력하시오:"))
wage = int(input("시간당 임금을 입력하시오:"))

if time <=40:
    totalWages = wage*time
else:
    totalWages = wage*40 + wage*1.5*(time-40)

print(f"총 임금은 {totalWages}")