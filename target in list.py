
nums=list(map(int,input().split()))#0 1 2 3 4
index=list(map(int,input().split()))#0 1 2 2 1
target=[]
for i in range(len(nums)):
    target.insert(index[i],nums[i])
print(target)
    
#output=[0, 4, 1, 3, 2]
