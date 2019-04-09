n=int(input())
res=''
for _ in range(n):
    s=input()
    if len(s)>len(res):
        res=s
print('The longest is:',res)
    
