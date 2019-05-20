def count(lst,layer,goal):
    re=0
    if layer==goal:
        for i in lst:
            if type(i)==type(1) or type(i)==type(1.0):
                re+=1
    else:
        for i in lst:
            if type(i)==type(list()):
                re+=count(i,layer+1,goal)
    return re

exec('lst='+input().strip())
n=int(input().strip())
print(count(lst,1,n))
