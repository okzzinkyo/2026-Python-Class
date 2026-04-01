# for i in range(10, 0, -1):
#     print("*"*i, end="\n")

for i in range(10, 0, -1):
    for star in range(i):
        print("*",end='')
    print()