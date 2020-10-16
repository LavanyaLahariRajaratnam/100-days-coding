c=list(map(int,input().split()))#2,3,5,1,3
n=int(input())#3
m=max(c)
l=[]
for i in range(0,len(c)):
    final=c[i]+n
    if final>=m:
        l.append(True)
    else:
        l.append(False)
print(l)



#sir
'''
l=[]
for i in a:
    if i+x>max(a):
        l.append(True)
    else:
        l.append(False)
print(l)
'''

#list comperision
'''
a=[2,3,5,1,3]
x=3
m=max(a)
l=[True if i+x>=m else False for i in a]
'''
