from collections import deque

def bfs(mapa, start, end, n, m):
    # Cola para BFS
    queue = deque([start])
    # Matriz para llevar el conteo de pasos
    pasos = [[-1] * m for _ in range(n)]
    pasos[start[0]][start[1]] = 0  # 0 pasos al iniciar

    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        # Si llegamos a la posición de Botas
        if (x, y) == end:
            return pasos[x][y]

        # Explorar las posiciones adyacentes
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            # Comprobar límites y si la posición es libre
            if 0 <= nx < n and 0 <= ny < m and mapa[nx][ny] != '*' and pasos[nx][ny] == -1:
                pasos[nx][ny] = pasos[x][y] + 1
                queue.append((nx, ny))

    # Si no se pudo llegar a la posición de Botas
    return -1

# Leer los tamaños de la matriz
n, m = map(int, input().split())

# Leer el mapa y encontrar las posiciones de Dora y Botas
mapa = []
dora_pos = None
botas_pos = None

for i in range(n):
    fila = input().strip()
    mapa.append(fila)
    if 'S' in fila:
        dora_pos = (i, fila.index('S'))
    if 'E' in fila:
        botas_pos = (i, fila.index('E'))

# Encontrar el número mínimo de pasos
resultado = bfs(mapa, dora_pos, botas_pos, n, m)

# Imprimir el resultado
print(resultado)
