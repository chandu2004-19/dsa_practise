def inverse_triangle(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print("*",end="")
        print()

num=int(input())
for i in range(num):
    a=int(input())
    inverse_triangle(a)