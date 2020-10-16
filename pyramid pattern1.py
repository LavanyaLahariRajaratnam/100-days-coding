'''
* * * * *
 * * * *
  * * *
   * *
    *
'''


n=int(input())
for i in range(n):
    print(("* "*(n-i)).center(2*n))
'''
    
n=8
for i in range(n,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(0,i):
        print("* ",end="")
    print()
'''
