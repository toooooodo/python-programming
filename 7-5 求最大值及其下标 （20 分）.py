n=input()
ls=list(map(int,input().rstrip().split()))
for i in range(len(ls)):
    if ls[i] == max(ls):
        break
print('%d %d'%(max(ls),i))
