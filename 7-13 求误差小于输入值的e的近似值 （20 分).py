import math

error=float(input())
_sum=1;i=1
while True:
    _sum+=(1/math.factorial(i))
    if 1/math.factorial(i)-1/math.factorial(i+1)<error:
        break
    i+=1
print("{:.6f}".format(_sum))
