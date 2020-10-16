def factors(x):
    for i in range(2, x//2 ):
        if x % i == 0:
            continue
    if (i==2 or i==3 or i==5):
        print("True")
            
    else:
        print("False")
num = int(input())
factors(num)
