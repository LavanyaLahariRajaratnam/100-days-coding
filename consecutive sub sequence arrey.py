'''
Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.
A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.
Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

Example 1:
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.

'''

def pattern():
    a=[1,2,4,4,4,4]#[1,2,1,2,1,1,3]
    m=2
    k=2
    i=0
    n=len(a)
    j=i+m
    c=0
    while j<n:
        if a[i]==a[j]:
            c+=1
            if c==m*(k-1):
                return True
        else:
            c=0
            i+=1
            j+=1
    return False
print(pattern())
            
