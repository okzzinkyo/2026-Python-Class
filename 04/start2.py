# for i in range(10):
#     print(" "*(10-i-1)+"*"*(i+1),end="\n")

for i in range(10):
    print(" "*(10-i-1),end='')
    for star in range(i+1): 
        print("*",end='')
    print()