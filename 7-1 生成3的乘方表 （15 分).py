import math
x=int(input().strip())
for i in range(x+1):
    print("pow(3,%d) = %d"%(i,math.pow(3,i)))
