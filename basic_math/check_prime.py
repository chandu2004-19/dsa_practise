def check_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=int(input())
for i in range(num):
    a=int(input())
    print(check_prime(a))