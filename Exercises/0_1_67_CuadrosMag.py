N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
expected_sum = sum(matrix[0])
diagonal1_sum = 0
diagonal2_sum = 0
is_semimagic = True
for i in range(N):
    if sum(matrix[i]) != expected_sum:
        is_semimagic = False
        break
    col_sum = 0
    for j in range(N):
        col_sum += matrix[j][i]    
    if col_sum != expected_sum:
        is_semimagic = False
        break
    diagonal1_sum += matrix[i][i]         
    diagonal2_sum += matrix[i][N - 1 - i] 

if diagonal1_sum != expected_sum or diagonal2_sum != expected_sum:
    is_semimagic = False
if is_semimagic:
    print(1)
else:
    print(0)