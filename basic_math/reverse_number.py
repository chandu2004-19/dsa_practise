def reverse_num(n):
    num=0
    while n!=0:
        last_dig=n%10
        n=n//10
        num=(num*10)+last_dig
    return num

num=int(input())
for i in range(num):
    a=int(input())
    print(reverse_num(a))