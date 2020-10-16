'''
given an integer n and an integer start. define an array nums where
nums[i]=start +2*i(0-indexed) and n==nums.length.
Return the bitwise XOR ("^") of all elements of nums.
'''

#sir
'''
n=int(input())#5
start=int(input())#0
for i in range(n):
    x^=s+(2*i)
print(x)
'''

n=int(input())
start=int(input())
l=[]
xor=0
for i in range(n):
    l.append(start+2*i)
for j in l:
    xor=xor^j
print(xor)
