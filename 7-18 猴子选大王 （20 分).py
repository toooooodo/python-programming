lst=[i+1 for i in range(int(input()))]
jdg=[True for i in range(len(lst))]
count=1
num=len(lst)
while num!=1:
    for i in range(len(lst)):
        if jdg[i]==True:
            if count==3:
                jdg[i]=False
                count=1
                num-=1
            else:
                count+=1
res=[i+1 for i in range(len(lst)) if jdg[i]==True]
print(res[0])
