m,n=map(int,input().strip().split())
matrix=[list(map(int,input().strip().split())) for i in range(m)]
flag=False
for i in range(1,m-1):
    for j in range(1,n-1):
        item=matrix[i][j]
        if item>matrix[i-1][j] and item>matrix[i+1][j] and item>matrix[i][j-1] and item>matrix[i][j+1]:
            flag=True
            print(item,i+1,j+1)
if not flag:
    print('None',m,n)
