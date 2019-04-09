x=int(input())
count=0
for i in range(x//5,0,-1):
    for j in range((x-5*i)//2,0,-1):
        k=x-5*i-2*j
        if k > 0:
            count+=1
            print("fen5:%d, fen2:%d, fen1:%d, total:%d"%(i,j,k,i+j+k))
print("count = {:d}".format(count))
