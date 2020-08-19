'''
n=int(input("enter a value"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('prime number')
else:
    print('not a prime number')
    
'''
'''
n=int(input("enter n value"))
count=0
i=1
while (i<=n):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('prime number')
else:
    print('not a prime number')
'''
'''

n=int(input("enter n value"))
for i in range(2,n):
    if n%i==0:
        print(n,'not a prime')
        break
else:
    print(n,'prime')
'''
'''
import math
n=int(input("Enter A Value"))
sq=int(math.sqrt(n))
for i in range(2,sq+1):
    if n%i == 0:
        print(n,"Is not prime number")
        break
else:
    print(n,"Is A Prime")
'''
import math
n=int(input('enter a number'))
i=2
while i<=abs(int(math.sqrt(n):
    if n%i==0:
        print(n,'is not prime')
        break
    i+=1
else:
    print(n,'is a prime')
