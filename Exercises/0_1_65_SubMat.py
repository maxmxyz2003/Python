def get_submatrix(matrix, start_row, start_col, size):
    """Extrae una submatriz de tamaño `size x size` a partir de (start_row, start_col)"""
    submatrix = []
    for i in range(size):
        submatrix.append(matrix[start_row + i][start_col:start_col + size])
    return submatrix

def multiply_matrices(M1, M2):
    """Multiplica dos matrices cuadradas de igual tamaño"""
    size = len(M1)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += M1[i][k] * M2[k][j]
    return result
def main():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    p, q = map(int, input().split())    
    submatrix_size = n // 2
    M1 = get_submatrix(A, 0, 0, submatrix_size)
    M2 = get_submatrix(A, 0, submatrix_size, submatrix_size)
    M3 = get_submatrix(A, submatrix_size, 0, submatrix_size)
    M4 = get_submatrix(A, submatrix_size, submatrix_size, submatrix_size)
    submatrices = [M1, M2, M3, M4]
    matrix_p = submatrices[p - 1]
    matrix_q = submatrices[q - 1]
    result = multiply_matrices(matrix_p, matrix_q)
    for row in result:
        print(" ".join(map(str, row)))
main()
