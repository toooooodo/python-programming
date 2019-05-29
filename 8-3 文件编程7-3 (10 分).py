srcFile=open('freedom.txt','rt')
dicFile=open('dic.txt','wt')

strs=srcFile.read()
for k in set([i for i in strs if i.isalnum()==False and i!='_']):
    strs=strs.replace(k,' ')
strs=strs.rstrip(' ').lower().split()
count=dict()
for i in strs:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
ans=sorted(count.items(),key=lambda x:(-x[1], x[0]))
for i in range(len(ans)):
    dicFile.write(ans[i][0]+': '+str(ans[i][1])+'\n')

srcFile.close()
dicFile.close()