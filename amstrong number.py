def armstrong(n):
    a=0
    n1=n
    while n>0:
        rem=n%10
        a+=rem*rem*rem
        n//=10
    
    if n1==a:
        return('Amstrong number')
    else:
        return('not a amstrong number')

n=int(input('enter a value'))
print(armstrong(n))
