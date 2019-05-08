exec('ls='+input().strip())
re=list(set(ls))
re.sort(key=ls.index)
print(' '.join(list(map(str,re))))