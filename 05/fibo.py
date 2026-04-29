def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end=' ')
        a, b=b, a+b
    print()


# 모듈 사용
# import fibo
# fibo.fib(100)
# 1 1 2 3 5 8 13 21 34 55 89 
# fibo.__name__
# 'fibo'
# fibo.__doc__
# from fibo import fib
# fib(1000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 