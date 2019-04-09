import math
n=int(input())
print('n={0:d},s={1:d}'.format(n,sum([math.factorial(i) for i in range(1,n+1,2)])))
