n=int(input())
matrix=[list(map(int,input().strip().split())) for i in range(n)]
print(sum([matrix[i][j] for i in range(n) for j in range(n) if i!=n-1 and j!=n-1 and i+j!=n-1]))
