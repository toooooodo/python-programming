import math

def judge(x):
    if x<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i==0:
                return False
    return True
    
n=int(input())
for i in range(n):
    x=int(input())
    if judge(x):
        print('Yes')
    else:
        print('No')
