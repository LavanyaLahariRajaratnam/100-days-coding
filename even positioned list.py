a=list(map(int,input().split()))
n=len(a)//2
l=[]
for i in range(0,len(a)//2):
    l.append(a[i])
    l.append(a[i+n])
print(l)
#output: [2,6,3,7,4,8,1,0]

