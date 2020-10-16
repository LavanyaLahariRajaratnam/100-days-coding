#Mine
'''

a={}
s1=input("student name")
s1marks1=int(input("marks1"))
s1marks2=int(input("marks2"))
s2=input("student name")
s2marks1=int(input("marks1"))
s2marks2=int(input("marks2"))
a={s1:[s1marks1,s1marks2],s2:[s2marks1,s2marks2]}
print(a)
'''
'''
a={}
n=int(input("enter key count"))
for i in range(1,n+1):#keys
    k=input("enter a key:")
    v=[]
    p=int(input("enter values count"))
    for j in range(p):#values
        m=int(input("enter marks"))
        v.append(m)
    a[k]=v
print(a)
    
'''

a={}
n=int(input("enter key count:"))
for i in range(1,n+1):
    k=input("enter a key:")
    a[k]=list(map(int,input().split()))
print(a)
