def fn(a,n):
    return sum([int(str(a)*i) for i in range(1,n+1)])
"""
/* 请在这里填写答案 */
"""
a,b=input().split()
s=fn(int(a),int(b))
print(s)