
a=list(map(int,input().split()))
k=sorted(a)
c=0
for i in range(len(a)):
    if k[i]!=a[i]:
        c+=1
print(c)
