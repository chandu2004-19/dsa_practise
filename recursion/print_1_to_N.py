def fun(i,n):
    if i>n:
        return
    print(i)
    fun(i+1,n)

num=int(input())
for i in range(num):
    a=int(input())
    fun(1,a)