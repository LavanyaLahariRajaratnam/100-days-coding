n=int(input('enter n value'))
r1=int(input('enter a value'))
r2=int(input('enter b value'))
if r1>r2:
    for i in range (r1,r2-1,-1):
        print(n,'*',i,'=',n*i)
else:
    for i in range (r1,r2+1):
        print(n,'*',i,'=',n*i)
