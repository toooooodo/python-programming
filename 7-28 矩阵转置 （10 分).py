lst=list(map(int,input().split()))
for i in range(3):
    print('{0:>4d}{1:>4d}{2:>4d}'.format(lst[i],lst[i+3],lst[i+6]))
