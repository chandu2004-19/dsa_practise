def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)

num=int(input())
for i in range(num):
    a=int(input())
    fun(a)