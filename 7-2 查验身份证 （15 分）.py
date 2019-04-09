weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m=['1','0','X','9','8','7','6','5','4','3','2']
n=int(input())
res=[]
for _ in range(n):
    str=list(input())
    sum=0
    flag = True
    for i in range(17):
        if '0'<=str[i]<='9':
            sum+=int(str[i])*weight[i]
        else:
            #res+=''.join(str)
            res.append(''.join(str))
            flag=False
            break
    if m[sum%11] != str[17] and flag==True:
        #res+=''.join(str)
        res.append(''.join(str))
if len(res)==0:
    print('All passed')
else:
    #print(len(res))
    for i in res:
        print(i)
