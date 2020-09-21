'''
def aliquot(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            print(i,end=" ")
            sum=sum+i
    print("sum - ",sum)       
    return sum       
n=int(input())
s=aliquotSeq(n)
if n!=s:
    while s!=1:
        s=aliquotSeq(s)


'''
'''
n=int(input())
print(n)
sum1=0
while(n>1 or sum1!=n):
    for  i in range(1,n//2+1):
        if(n%i==0):
            sum1+=i
    n=sum1
    sum1=0
    print(n)
'''

def aliquot(n):
    while n>1:
        sum=0
        for i in range (1,n):
            if(n%i==0):
                sum=sum+i
        print(sum)
        if n==sum:
            break
        n=sum
n=int(input('enter a number :'))
aliquot(n)
