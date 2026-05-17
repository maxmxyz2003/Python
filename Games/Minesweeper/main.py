def contar_minas_adjacentes(campo, M, N):
    salida = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if campo[i][j] == 1:
                salida[i][j] = 9
                for x in range(max(0, i-1), min(i+2, M)):
                    for y in range(max(0, j-1), min(j+2, N)):
                        if salida[x][y] != 9:
                            salida[x][y] += 1                            
    return salida
M, N = map(int, input().split())
campo = []
for _ in range(M):
    campo.append(list(map(int, input().split())))
resultado = contar_minas_adjacentes(campo, M, N)
for fila in resultado:
    print(" ".join(map(str, fila)))
