def palindrome(i,j):
    if i>=j:
        return True
    if a[i]==a[j]:
        return palindrome(i+1,j-1)
    return False

num=int(input())
for i in range(num):
    a=input()
    print(palindrome(0,len(a)-1))