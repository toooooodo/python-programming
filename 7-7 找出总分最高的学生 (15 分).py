n=int(input().strip())
lst=[]
M=mid=-1
for i in range(n):
    lst.append(list(input().strip().split()))
    lst[i][2]=int(lst[i][2])+int(lst[i][3])+int(lst[i][4])
    del lst[i][3]
    del lst[i][3]
for i in range(n):
    if lst[i][2]>M:
        M=lst[i][2]
        mid=i
print(lst[mid][1],lst[mid][0],lst[mid][2])