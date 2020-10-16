'''
i/p=[2 5 3 4 2]===>/\/\=== 2<5>3<4>2 True
o/p= True or yes

[2 5 6 3 4]===>2<5<6 False
False or no
'''

a=[2,3,1,5,3]
status=True
for i in range(len(a)-1):
    if a[i]<a[i+1] and i%2==0:
        status=True
    elif a[i]>a[i+1] and i%2==1:
        status=True
    else:
        status=False
        break
print(status)

'''
l=[2,3,1,5,3] 
print(l)
for i in range(0,len(l)-2,2):
    if not (l[i],l[i+2]):
        print("False")
       break
   else:
       print("True")
'''
