def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

n=int(input())
for j in range(n):
    a=int(input())
    square(a)