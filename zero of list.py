
a=[1,0,2,3,0,4,5,0]
l=[]
for i in range(len(a)):
    if a[i]==0:
        l.append(a[i])
    if len(l)==len(a):
        break
    else:
        l.append(a[i])
print(l)
print("null")

