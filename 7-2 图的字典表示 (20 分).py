n=int(input())
v_num=l_num=l_tot=0
for _ in range(n):
    exec('d = '+input())
    for v,re in d.items():
        v_num+=1
        for to_v,edge in re.items():
            l_num+=1
            l_tot+=edge
print(v_num,l_num,l_tot)