def recoger_bebes(n, eventos):
    fila = []
    resultado = []
    
    for evento in eventos:
        tipo, nombre = evento.split()
        if tipo == 'F':
            fila.append(nombre)
        elif tipo == 'B':
            mujer = fila.pop()
            resultado.append(f"{nombre} {mujer}")
    
    return resultado

def main():
    N = int(input())
    eventos = [input().strip() for _ in range(N)]
    resultados = recoger_bebes(N, eventos)
    for resultado in resultados:
        print(resultado)

main()
