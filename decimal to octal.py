n=int(input())
b=''
while n:
    b+=str(n%8)
    n=n//8
    #print(n)
print(b[::-1])
