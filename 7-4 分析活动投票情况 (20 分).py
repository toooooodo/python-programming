ls=list(map(int,input().strip().split(',')))
s=set()
full_s={6,7,8,9,10}
for i in ls:
    if i in full_s:
        s.add(i)
diff=sorted(list(full_s-s))
print(' '.join(list(map(str,diff))))