n=int(input())
matrix=[list(map(int,input().strip().split())) for i in range(n)]
for i in range(n):
    #index=matrix[i].index(max(matrix[i]))
    index=0
    for j in range(1,n):
        if matrix[i][j]>=matrix[i][index]:
            index=j
    flag=True
    for j in range(n):
        if matrix[j][index]<matrix[i][index]:
            flag=False
            break
    if flag==True:
        print(i,index)
        break
else:
    print('NONE')
