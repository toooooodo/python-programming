def lstsum(lst):
    re=0
    for i in lst:
        if type(i)==type(list()) or type(i)==type(tuple()):
            re+=lstsum(i)
        elif type(i)==type(1) or type(i)==type(1.0):
            re+=i
    return re

exec('lst='+input().strip())
print(lstsum(lst))