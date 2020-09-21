#mine

n=int(input())
c=0
for i in range(0,n+1):
    rem=n%10
    c+=(rem*2**i)
    n=n//10
print(c)
    
    
'''

n=111
d=0
b=1
while n:
    r=n%10
    n=n//10
    d+=r*b
    b*=2
print(d)
'''
