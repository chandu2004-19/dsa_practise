def count_dig(n):
    c=0
    while n!=0:
        c+=1
        n=n//10
    return c
     

num=int(input())
for i in range(num):
    a=int(input())
    print(count_dig(a))