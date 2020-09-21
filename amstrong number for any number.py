#counting no of digits
'''

def digits():
    count=0
    i=0
    while n>0:
        count+=1
        n=n//10
    return count
 '''     
'''
def armstrong(n):
    l=1
    while n% 10** 1!=n:
        l+=1
    res=0
    temp=n
    while n>0:
        res+=(n%10)**1
        n//=10
    return res==temp
print(armstrong(int(input())))
 '''
    

