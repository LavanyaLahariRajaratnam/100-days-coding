'''
l=[2,0,5,0,4,5]
for i in range(0,len(l)):
    if l[i] == 0:
       l.pop(i)
       l.append(0)
print(l)
'''

a=[2,0,5,0,4,5]
c=0#1
for i in range(len(a)):#0,1,2
    if a[i]!=0:#2,5
        m=a[i]#2,5
        a[i]=a[c]#2,0
        a[c]=m#2,5
        c+=1
print(a)

#i=1 2 0 5 0 4 5
#i=2 2 5 0 0 4 5
#i=3 2 5 4 0 0 5
#i=4 2 5 4 5 0 0
