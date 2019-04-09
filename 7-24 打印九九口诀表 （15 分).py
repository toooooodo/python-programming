n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('{0:d}*{1:d}={2:<4d}'.format(j,i,j*i),end='')
    print()
