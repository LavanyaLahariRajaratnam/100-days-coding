#with Recursion
'''
def sumFib(n):
   a,b = 0,1
   while n >= b :
         if n==b:
            return b
         a,b = b,a+b
   print(a)
   return sumFib(n-a)
print(sumFib(int(input())))


'''
#Without Recursion

n=int(input())
def grtprevfib(n):
   a=0
   b=1
   while(n>=b):
      a,b=b,a+b
   return a
def fib(n):
   a=0
   b=1
   for i in range(n+1):
      a,b=b,a+b
      if a==n:
         return True
   else:
      return False
def fibsum(n):
   s=0
   while n:
      if fib(n):
         print(n)
         break
      else:
         x=grtprevfib(n)
         n-=x
         print(x)
fibsum(n)
