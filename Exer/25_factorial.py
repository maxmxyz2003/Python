from math import factorial


def fact (numero):
    if numero==1:
        return 1
    else:
        return factorial(numero)


numero=6
resultado=factorial(numero)
print(f"El resultasdo del factorial de 6 es: {resultado}")

