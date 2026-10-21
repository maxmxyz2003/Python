# Leer los tamaños de los conjuntos
M, N = map(int, input().split())
# Leer los elementos de los conjuntos
A = set(map(int, input().split()))
B = set(map(int, input().split()))
# Comparar los conjuntos
if A == B:
    print("A = B")
elif A < B:  # A está incluido propiamente en B
    print("A < B")
elif B < A:  # B está incluido propiamente en A
    print("A > B")
else:
    print("A != B")
