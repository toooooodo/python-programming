lst=list(map(int,input().strip().split()))
for i in range(3):
    print('{0:>4d}{1:>4d}{2:>4d}{3:>4d}{4:>4d}'.format(lst[i*3],lst[i*3+1],lst[i*3+2],max(lst[i*3:(i+1)*3]),sum(lst[i*3:(i+1)*3])))
