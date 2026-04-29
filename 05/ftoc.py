def FtoC(temp_f):
    temp_c = 5 * (temp_f-32.0) / 9
    return temp_c

temp_f = float(input("화씨 온도?"))
print(FtoC(temp_f))