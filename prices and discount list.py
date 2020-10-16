
p=[8,4,6,2,3]#list(map(int,input().split()))
l=[]
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j]:
            l.append(p[i]-p[j])
            break
    else:
        l.append(p[i])
print(l)

'''
l=[8,4,6,2,3]
k=[]
for i in range(len(l)):
    for j in range(i,len(l)):
       if l[i]>=l[j] and i!=j:
           k.append(l[i]-l[j])
           break
       else:
           k.append(l[i])
print(k)
'''
'''
a=list(map(int,input().split()))
b=[]
c=len(a)
for i in range(0,c):
    for j in range(i+1,c):
       if a[i]<a[j]:
           b.append(a[i]-a[j])
          break
       else:
           b.append(a[i])
print(b)
'''
