n=int(input())
b=' '
while n:
    b+=str(n%2)
    n=n//2
print(b[::-1])
