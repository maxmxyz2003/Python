n = int(input())
conexiones = {i: [] for i in range(10)}
for _ in range(n):
    a, b = map(int, input().split())
    conexiones[a].append(b)
    conexiones[b].append(a)
p = int(input())
casas_conectadas = sorted(conexiones[p])
print(' '.join(map(str, casas_conectadas)))
