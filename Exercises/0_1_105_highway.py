n = int(input())
carreteras = set()
for _ in range(n):
    a, b = map(int, input().split())
    carreteras.add((a, b))
    carreteras.add((b, a))
q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    if (s, e) in carreteras:
        print("YES")
    else:
        print("NO")
