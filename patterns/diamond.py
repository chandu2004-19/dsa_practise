def diamond(n):
    for i in range(2*n):
        if i<n:
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
        else:
            for j in range(i-n):
                print(" ",end="")
            for j in range(2*n-2*(i-n)-1):
                print("*",end="")
        print()

num=int(input())
for i in range(num):
    a=int(input())
    diamond(a)