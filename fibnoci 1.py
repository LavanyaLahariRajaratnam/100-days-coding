'''
def fib(n):
    a=0
    b=1
    s=a+b
    print(a,b,end='')
    i=2
    while i<n:
        c=a+b
        s+=c
        print(c,end=" ")
        a=b
        b=c
        i+=1
        print(s)
fib(10)

'''

'''
#  n th positin of fibnoci


n=int(input())
def fib(n):
    a=0
    b=1
    i=2
    while i<n:
        c=a+b
        #print(c,end=" ")
        a=b
        b=c
        i+=1
    print(b)
fib(n)
'''
# recurrsive of fibnoci
n=int(input())
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
print(fib(n))
