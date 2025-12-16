def triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()

num=int(input())
for j in range(num):
    a=int(input())
    triangle(a)