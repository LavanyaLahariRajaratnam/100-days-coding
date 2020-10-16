def getMaxLength(n,arr):
    count = 0 
    result = 0 
    for i in range(0, n): 
        if (arr[i] == 0): 
            count = 0
        else: 
            count+= 1 
            result = max(result, count)  
    return result
n=int(input())
arr=list(map(int,input().split()))
print(getMaxLength(n,arr))
