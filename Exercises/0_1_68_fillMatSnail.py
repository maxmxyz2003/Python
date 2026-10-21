m, n = map(int, input().split())
matrix = [[0] * n for _ in range(m)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0 
row, col = 0, 0
for num in range(1, m * n + 1):
    matrix[row][col] = num
    next_row = row + directions[current_direction][0]
    next_col = col + directions[current_direction][1]
    if not (0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == 0):
        current_direction = (current_direction + 1) % 4
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]
    row, col = next_row, next_col
for row in matrix:
    print(" ".join(map(str, row)))
