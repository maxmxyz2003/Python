def dfs(mapa, i, j, M, N):
    # Comprobar límites y si el lugar es agua o ya está visitado
    if i < 0 or i >= M or j < 0 or j >= N or mapa[i][j] == 'W':
        return
    # Marcar la posición como agua para no contarla de nuevo
    mapa[i][j] = 'W'
    # Llamar recursivamente a DFS para las posiciones adyacentes
    dfs(mapa, i - 1, j, M, N)  # Arriba
    dfs(mapa, i + 1, j, M, N)  # Abajo
    dfs(mapa, i, j - 1, M, N)  # Izquierda
    dfs(mapa, i, j + 1, M, N)  # Derecha

# Leer los tamaños de la matriz
M, N = map(int, input().split())

# Leer la matriz
mapa = [list(input().strip()) for _ in range(M)]

# Contar las islas
islas = 0

for i in range(M):
    for j in range(N):
        if mapa[i][j] == 'L':  # Encontrar una nueva isla
            islas += 1
            dfs(mapa, i, j, M, N)  # Marcar toda la isla

# Imprimir el número de islas
print(islas)
