n=int(input())
c=0
for i in range(0,n+1):
    rem=n%10
    c+=(rem*8**i)
    n=n//10
print(c)
