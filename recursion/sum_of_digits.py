def sum_of_digits(n,s):
    if n==0:
        return s 
    s+=(n%10)
    return sum_of_digits(n//10,s)

num=int(input())
for i in range(num):
    a=int(input())
    print(sum_of_digits(a,0))
    