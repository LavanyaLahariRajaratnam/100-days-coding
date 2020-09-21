#Without Recursion
'''

n=int(input('enter a number'))
print(n)
while n!=1:
    if n%2==0:
        a=n//2
        print(a)
        n=a
    else:
        a=n*3+1
        print(a)
        n=a
        
'''
#with recursion
n=int(input('enter a number'))
def col_seq(n):
    if n==1:
        return str(1)
    else:
        if n%2==0:
            a=n//2
            return(str(n)+" "+col_seq(a))
            #n=a
        
        else:
            a=n*3+1
            return(str(n)+" "+col_seq(a))
            #n=a
          
print(col_seq(n))


