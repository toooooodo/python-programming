import itertools


n=int(input().strip())
lst=[i for i in range(1,n+1)]
lst=list(map(str,lst))
per=list(itertools.permutations(lst,n))
for i in per:
    print(''.join(list(i)))