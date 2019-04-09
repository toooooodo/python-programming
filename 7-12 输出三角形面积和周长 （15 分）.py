a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if a+b<=c or a+c<=b or b+c<=a:
    print("These sides do not correspond to a valid triangle")
else:
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("area = %.2f; perimeter = %.2f"%(area,s*2))
