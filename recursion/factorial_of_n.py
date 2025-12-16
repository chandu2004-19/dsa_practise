def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

num=int(input())
for i in range(num):
    a=int(input())
    print(fact(a))