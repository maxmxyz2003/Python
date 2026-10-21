p1=int(input())
p2=int(input())
p3=int(input())
p4=int(input())
if p1 <= p3 <= p2 <= p4 or p3 <= p1 <= p4 <= p2:
    print(1)
else:
    print(0)
