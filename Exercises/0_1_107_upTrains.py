from collections import deque
n, m = map(int, input().split())
grafo = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)
start, end = map(int, input().split())
def bfs_min_paradas(start, end):
    queue = deque([start])
    paradas = [-1] * n
    paradas[start] = 0  # 0 paradas al iniciar
    while queue:
        ciudad_actual = queue.popleft()
        if ciudad_actual == end:
            return paradas[ciudad_actual]
        for vecino in grafo[ciudad_actual]:
            if paradas[vecino] == -1:  # Si no hemos visitado este vecino
                paradas[vecino] = paradas[ciudad_actual] + 1
                queue.append(vecino)
    return "Imposible"
resultado = bfs_min_paradas(start, end)
print(resultado)
