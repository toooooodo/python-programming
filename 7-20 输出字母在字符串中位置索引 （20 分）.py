s=input()
ls=list(input().split())
ls.reverse()
for i in ls:
    for j in range(len(s)-1,-1,-1):
        if s[j]==i:
            print('%d %s'%(j,i))
