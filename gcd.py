'''
a=int(input('a'))
b=int(input('b'))
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if (a%i==0 and b%i==0):
        gcd=i
print(gcd)



'''
'''
a=int(input('a'))
b=int(input('b'))

for i in range(1,4):
    if (a//i==0 and b//i==0):
        lcm=i
print(lcm)
'''

n=int(input('enter a number'))
m=int(input('enter a number'))
greater=max(n,m)
while(True):
    if(greater%n==0 and greater%m==0):
        print("lcm=",greater)
        break
    greater+=1

