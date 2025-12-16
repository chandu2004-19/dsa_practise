def gcd(a,b):
    while (a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a

num=int(input())
for i in range(num):
    a=int(input())
    b=int(input())
    print(gcd(a,b))