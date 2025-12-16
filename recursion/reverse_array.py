def reverse(i,j):
    if i>=j:
        return 
    a[i],a[j]=a[j],a[i]
    reverse(i+1,j-1)

num=int(input())
for i in range(num):
    n=int(input())
    a=list(map(int,input().split()))
    reverse(0,n-1)
    print(a)
    