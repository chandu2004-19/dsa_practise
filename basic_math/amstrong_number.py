def check_amstrong(n):
    l=len(str(n))
    temp=n
    num=0
    while n!=0:
        last_dig=n%10
        n=n//10
        num+=(last_dig**l)
    if temp==num:
        return True
    return False

num=int(input())
for i in range(num):
    a=int(input())
    print(check_amstrong(a))
    