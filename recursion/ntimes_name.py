def ntimes(n,name):
    if n==0:
        return 
    print(name)
    ntimes(n-1,name)

num=int(input())
for i in range(num):
    a=int(input())
    name=input()
    ntimes(a,name)