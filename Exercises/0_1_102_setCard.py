N, M = map(int, input().split())
conjunto = set()
for _ in range(M):
    evento = input().split()
    tipo = evento[0]
    if tipo == 'I':
        valor = int(evento[1])
        conjunto.add(valor)
    elif tipo == 'E':
        valor = int(evento[1])
        conjunto.discard(valor)
    elif tipo == 'C':
        print(len(conjunto))
