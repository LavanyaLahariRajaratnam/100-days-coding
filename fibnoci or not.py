
n=int(input())
a=0
b=1
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    if b==n:
        break
if b==n:
    print('fibnocci')
else:
    print('not a fibnocci')

