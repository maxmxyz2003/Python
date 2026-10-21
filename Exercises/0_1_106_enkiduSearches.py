N = int(input())
distancias = [list(map(int, input().split())) for _ in range(N)]
visitadas = [False] * N
visitadas[0] = True  # Gilgamesh comienza en la ciudad 1 (índice 0)
orden_visita = []
for _ in range(N - 1):
    ciudad_actual = 0  # Siempre empieza desde la ciudad 1 (índice 0)
    ciudad_siguiente = -1
    distancia_minima = float('inf')
    for ciudad in range(N):
        if not visitadas[ciudad] and distancias[ciudad_actual][ciudad] < distancia_minima:
            ciudad_siguiente = ciudad
            distancia_minima = distancias[ciudad_actual][ciudad]
        elif not visitadas[ciudad] and distancias[ciudad_actual][ciudad] == distancia_minima:
            ciudad_siguiente = min(ciudad_siguiente, ciudad)
    visitadas[ciudad_siguiente] = True
    orden_visita.append(ciudad_siguiente + 1)  # Almacenar en base 1
print(" ".join(map(str, orden_visita)))
