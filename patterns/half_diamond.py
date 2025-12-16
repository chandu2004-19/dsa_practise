def half_diamond(n):
    for i in range(2*n-1):
        if i<n:
            for j in range(i+1):
                print("*",end="")
        else:
            for j in range(2*n-i-1):
                print("*",end="")
        print()

num=int(input())
for i in range(num):
    a=int(input())
    half_diamond(a)