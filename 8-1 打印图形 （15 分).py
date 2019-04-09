x=5
for i in range(1,x+1):
    print('*'*i)
for i in range(1,x+1):
    print(' '*(x-i),end='')
    print('*'*(i*2-1))
for i in range(1,x+1):
    if i<=(x+1)//2:
        print(' '*((x+1)//2-i),end='')
        print('*'*(2*i-1))
    else:
        mid=(x+1)//2
        print(' '*(i-mid),end='')
        print('*'*((x-i)*2+1))
