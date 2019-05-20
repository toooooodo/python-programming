def count(lst,layer):
    re=0
    for i in lst:
        if type(i)==type(1) or type(i)==type(1.0):
            re+=layer
        elif type(i)==type(list()):
            re+=count(i,layer+1)
    return re
exec('lst='+input().strip())
print(count(lst,1))