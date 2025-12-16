def triangle(n):
    for i in range(n):
        if i%2==0:
            for j in range(i+1):
                if j%2==0:
                    print("1",end="")
                else:
                    print("0",end="")
        else:
            for j in range(i+1):
                if j%2==0:
                    print("0",end="")
                else:
                    print("1",end="")
        print()
num=int(input())
for i in range(num):
    a=int(input())
    triangle(a)