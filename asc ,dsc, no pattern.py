



'''
n = input()
asC = n[0] <= n[1]
dsC = n[0] >= n[1]
i = 1
while (asC or dsC) and i<len(n)-1:
	if asC:
		asC = n[i] <= n[i+1]
	elif dsC:
		dsC = n[i] >= n[i+1]
	i+=1
if asC:
		print("Assending")
elif dsC:
		print("Desending")
else:
		print("No order")
'''

n=int(input('enter a number:'))
ac=0
dc=0
x=10
y=0
cnt=0
while n:
        r=n%10
        n//=10
        cnt+=1
        if x>r:
                x=r
                dc+=1
        if y<r:
                y=r
                ac+=1
if dc==cnt:
        print('ascending')
elif ac==cnt:
        print('descending')
else:
        print('no order')
        
