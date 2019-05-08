x1=int(input())
oper=input()
x2=int(input())
if oper=='/':
    if x2==0:
        print('divided by zero')
    else:
        print('%.2f'%(x1/x2))
elif oper=='*':
    print('%.2f'%(x1*x2))
elif oper=='+':
    print('%.2f'%(x1+x2))
else:
    print('%.2f'%(x1-x2))