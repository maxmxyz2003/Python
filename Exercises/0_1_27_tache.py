numero = int(input())

for i in range(numero):
    for j in range(numero):
        if j == i or j == (numero - i - 1):
            print("@", end="")
        else:
            print(" ", end="")
    print()
