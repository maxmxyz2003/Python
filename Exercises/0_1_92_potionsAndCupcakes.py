def calcular_altura_final(A, acciones):
    pila = []
    altura = A

    for accion in acciones:
        if accion[0] == 'C':
            H = int(accion[1])
            pila.append(H)
            altura += H
        elif accion[0] == 'D':
            if pila:
                altura -= pila.pop()
    
    return altura

A, N = map(int, input().split())
acciones = [input().split() for _ in range(N)]
resultado = calcular_altura_final(A, acciones)
print(resultado)
