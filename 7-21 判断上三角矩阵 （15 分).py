t=int(input())
for i in range(t):
    n=int(input())
    flag=True
    for j in range(n):
        lst=input().strip().split()
        for k in range(j):
            if lst[k]!='0':
                flag=False
                break
    if flag==True:
        print('YES')
    else:
        print('NO')
