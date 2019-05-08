#a,b=int(input().strip().split())
a,b=map(int,input().strip().split())
print(len([i for i in range(a,b+1) if i%3==0 and i%5==0 and i%7==0]))    