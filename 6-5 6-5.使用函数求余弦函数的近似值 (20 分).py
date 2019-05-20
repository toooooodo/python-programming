import math
def funcos(eps,x):
    re=0
    i=0
    while True:
        added=((-1)**(i/2))*(x**i)/math.factorial(i)
        if math.fabs(added)<eps:
            break
        re+=added
        i+=2
    return re

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))