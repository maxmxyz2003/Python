#include <stdio.h>
m=n=0
m=int(input())
n=int(input())

matrix = [[0] * n for _ in range(m)]
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for j in range(n):
    for i in range(m):
        print(matrix[i][j])
        if (i<m-1):
            print(" ",end="")
        print("")

# https://omegaup.com/profile/cheeto/
