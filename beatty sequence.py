#mine
#without Recursion
'''
import math as m
n=int(input('enter n value'))
for i in range(1,n+1):
    a=i*m.sqrt(2)
    b=m.floor(a)
    print(b)
    
'''

def beatty(n):
    for i in range(1,n+1):
        a=int(i*(2**0.5))
        print(a)
n=int(input('enter n value'))
beatty(n)
