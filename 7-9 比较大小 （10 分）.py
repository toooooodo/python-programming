a=list(input().split())
a=list(map(int,a))
a.sort()
for i in range(len(a)):
    if i != len(a)-1:
        print(str(a[i])+"->",end="")
    else:
        print(str(a[i]))
