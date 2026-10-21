def dfs(mapa, i, j, n, m):
    # Comprobar límites y si la posición es un espacio libre
    if i < 0 or i >= n or j < 0 or j >= m or mapa[i][j] != '.':
        return
    # Marcar la posición como visitada
    mapa[i][j] = '#'
    # Llamar recursivamente a DFS para las posiciones adyacentes
    dfs(mapa, i - 1, j, n, m)  # Arriba
    dfs(mapa, i + 1, j, n, m)  # Abajo
    dfs(mapa, i, j - 1, n, m)  # Izquierda
    dfs(mapa, i, j + 1, n, m)  # Derecha

# Leer los tamaños de la matriz
n, m = map(int, input().split())

# Leer el mapa
mapa = [list(input().strip()) for _ in range(n)]

# Encontrar la posición inicial de Dora
for i in range(n):
    for j in range(m):
        if mapa[i][j] == '#':
            dora_x, dora_y = i, j
            break

# Marcar las áreas accesibles desde la posición de Dora
dfs(mapa, dora_x, dora_y, n, m)

# Imprimir el mapa resultante
for fila in mapa:
    print(''.join(fila))
