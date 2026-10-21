# Leer los números de vértices y operaciones
N, M = map(int, input().split())

# Usar un conjunto para almacenar las aristas
aristas = set()

# Procesar cada operación
for _ in range(M):
    operacion = input().split()
    tipo = operacion[0]
    I = int(operacion[1])

    if tipo == 'A':
        J = int(operacion[2])
        # Agregar o quitar la arista (I, J)
        if (I, J) in aristas:
            aristas.remove((I, J))
        else:
            aristas.add((I, J))
    
    elif tipo == 'V':
        # Si se ejecuta la operación V, quitar todas las aristas de I
        for j in range(N):
            if j != I:
                aristas.discard((I, j))  # Quitar aristas hacia I desde j
                aristas.discard((j, I))  # Quitar aristas hacia j desde I
        # Agregar aristas desde I hacia todos los demás vértices
        for j in range(N):
            if j != I:
                aristas.add((I, j))  # Agregar aristas hacia j desde I

# Imprimir las aristas resultantes
for (u, v) in aristas:
    print(u, v)
