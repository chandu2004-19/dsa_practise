def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

num=int(input())
for i in range(num):
    a=int(input())
    triangle(a)