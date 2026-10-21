def procesar_instrucciones(C, D, instrucciones):
    pila = []
    resultados = []
    for instruccion in instrucciones:
        partes = instruccion.split()
        comando = partes[0]
        if comando == "PONTE":
            if len(pila) < C:
                coraza = partes[1]
                pila.append(coraza)
                resultados.append(coraza)
            else:
                resultados.append("IMPOSIBLE")
        elif comando == "QUITA":
            if pila:
                coraza = pila.pop()
                resultados.append(coraza)
            else:
                resultados.append("IMPOSIBLE")
    return resultados
def main():
    C, D = map(int, input().split())
    instrucciones = [input().strip() for _ in range(D)]
    resultados = procesar_instrucciones(C, D, instrucciones)
    for resultado in resultados:
        print(resultado)

main()
