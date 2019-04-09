import math

n=int(input())
_sum=sum([1/math.factorial(i) for i in range(n+1)])
print("%.8f"%(_sum))
