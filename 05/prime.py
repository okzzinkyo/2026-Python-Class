def isPrime(number):
    for n in range(2,number):
        if(number % n == 0):
            return False
    return True;
    
number = int(input("정수를 입력하시오"))
print(isPrime(number))
