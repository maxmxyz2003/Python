# Paso 1: Leer la entrada
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A_prime = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_prime[j][N-1-i] = A[i][j]
for row in A_prime:
    print(" ".join(map(str, row)))
