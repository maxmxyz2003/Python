def calcular_descuento(precios, platos_rotos):
    descuento_total = 0    
    for plato in platos_rotos:
        tipo_vajilla = plato[0]  # A, B, C o D
        tamaño_plato = int(plato[1]) - 1  # 1, 2, 3, 4 (convertimos a índice 0, 1, 2, 3)
        # Mapear tipo de vajilla a índice de fila en la matriz
        if tipo_vajilla == 'A':
            fila = 0
        elif tipo_vajilla == 'B':
            fila = 1
        elif tipo_vajilla == 'C':
            fila = 2
        elif tipo_vajilla == 'D':
            fila = 3
        descuento_total += precios[fila][tamaño_plato]
    return descuento_total

precios = []
for _ in range(4):
    fila = list(map(int, input().split()))
    precios.append(fila)
N = int(input())
platos_rotos = [input() for _ in range(N)]
descuento = calcular_descuento(precios, platos_rotos)
print(descuento)
