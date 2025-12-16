def palindrome_check(n):
    temp=n
    num=0
    while n!=0:
        last_dig=n%10
        n=n//10
        num=(num*10)+last_dig
    if num==temp:
        return True
    return False

num=int(input())
for i in range(num):
    a=int(input())
    print(palindrome_check(a))