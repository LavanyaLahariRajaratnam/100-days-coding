
num = input()

def digitalroot(num):
    if len(num) == 1:
        return num
    else:
        sum = 0
        for i in num:
            sum += int(i)
        num = str(sum)
        return digitalroot(num)
        
print(digitalroot(num))
