def inverse_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()

num=int(input())
for i in range(num):
    a=int(input())
    inverse_triangle(a)
