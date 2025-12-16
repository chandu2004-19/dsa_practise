def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

num=int(input())
for i in range(num):
    a=int(input())
    print(fib(a))