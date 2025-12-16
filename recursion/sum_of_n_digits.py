def sum_of_n_digits(n):
    if n==0:
        return 0
    return n+sum_of_n_digits(n-1)

num=int(input())
for i in range(num):
    a=int(input())
    print(sum_of_n_digits(a))