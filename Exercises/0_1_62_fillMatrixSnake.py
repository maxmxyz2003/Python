def matriz_serpentina(M, N):
    matriz = [[0 for _ in range(N)] for _ in range(M)]
    contador = 1
    for i in range(M):
        if i % 2 == 0:
            for j in range(N):
                matriz[i][j] = contador
                contador += 1
        else:
            for j in range(N-1, -1, -1):
                matriz[i][j] = contador
                contador += 1
    for fila in matriz:
        print(" ".join(map(str, fila)))
M, N = map(int, input().split())
matriz_serpentina(M, N)
