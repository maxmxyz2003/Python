from math import *
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])
    # Comprobación de las dimensiones (número de columnas de A debe ser igual al número de filas de B)
    if colsA != rowsB:
        return "No se pueden multiplicar las matrices: dimensiones incompatibles."
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result
punt0= [[3],[3],[3],[1]]
punt1= [[5],[1.5],[2],[1]]
punt2= [[3.5],[-1],[2],[1]]
punt3= [[-1],[-2],[3],[1]]
angleRx=35
angleRy=70
angleRz=-65
mpx=(punt0[0][0]+punt1[0][0]+punt2[0][0]+punt3[0][0])/4
mpy=(punt0[1][0]+punt1[1][0]+punt2[1][0]+punt3[1][0])/4
mpz=(punt0[2][0]+punt1[2][0]+punt2[2][0]+punt3[2][0])/4
angleRx=angleRx*pi/180
angleRy=angleRy*pi/180
angleRz=angleRz*pi/180
sx=0.5
sy=0.5
sz=0.5
originT = [
    [1, 0, 0,-1*mpx],
    [0, 1, 0,-1*mpy],
    [0, 0, 1,-1*mpz],
    [0, 0, 0,1]]
originalPos = [
    [1, 0, 0,mpx],
    [0, 1, 0,mpy],
    [0, 0, 1,mpz],
    [0, 0, 0,1]
]
moveMat = [
    [1, 0, 0,-4],
    [0, 1, 0,2],
    [0, 0, 1,1.5],
    [0, 0, 0,1]
]

scaleMat= [
    [sx, 0, 0,0],
    [0, sy, 0,0],
    [0, 0, sz,0],
    [0, 0, 0,1]
]
Rx = [
    [1, 0, 0,0],
    [0, cos(angleRx), -1*sin(angleRx),0],
    [0, sin(angleRx), cos(angleRx),0],
    [0, 0, 0,1]
]
Ry = [
    [cos(angleRy), 0, sin(angleRy),0],
    [0, 1, 0,0],
    [-1*sin(angleRy), 0, cos(angleRy),0],
    [0, 0, 0,1]
]
Rz=[
    [cos(angleRz), -1*sin(angleRz), 0,0],
    [sin(angleRz), cos(angleRz), 0,0],
    [0, 0, 1,0],
    [0, 0, 0,1]
]
# result = multiply_matrices(moveMat,multiply_matrices(scaleMat,multiply_matrices(originalPos,multiply_matrices(Rz,multiply_matrices(Ry,multiply_matrices(Rx, multiply_matrices(originT, punt3)))))))
result = multiply_matrices(moveMat,multiply_matrices(scaleMat,multiply_matrices(originalPos,multiply_matrices(Rz,multiply_matrices(Ry,multiply_matrices(Rx, multiply_matrices(originT, punt0)))))))
print("P1:")
print("(",end="")
for i in result:
    for j in i:
        print(round(j,2), end=", ")
print(")")

result = multiply_matrices(moveMat,multiply_matrices(scaleMat,multiply_matrices(originalPos,multiply_matrices(Rz,multiply_matrices(Ry,multiply_matrices(Rx, multiply_matrices(originT, punt1)))))))
print("P2:")
print("(",end="")
for i in result:
    for j in i:
        print(round(j,2), end=", ")
print(")")
result = multiply_matrices(moveMat,multiply_matrices(scaleMat,multiply_matrices(originalPos,multiply_matrices(Rz,multiply_matrices(Ry,multiply_matrices(Rx, multiply_matrices(originT, punt2)))))))
print("P3:")
print("(",end="")
for i in result:
    for j in i:
        print(round(j,2), end=", ")
print(")")
result = multiply_matrices(moveMat,multiply_matrices(scaleMat,multiply_matrices(originalPos,multiply_matrices(Rz,multiply_matrices(Ry,multiply_matrices(Rx, multiply_matrices(originT, punt3)))))))
print("P4:")
print("(",end="")
for i in result:
    for j in i:
        print(round(j,2), end=", ")
print(")")


"""
import numpy as np
# Definición de matrices usando numpy
matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixB = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# Multiplicación de matrices
result = np.dot(matrixA, matrixB)
# Muestra del resultado
print("Resultado usando numpy:")
print(result)
"""