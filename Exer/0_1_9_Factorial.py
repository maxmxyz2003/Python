numeros_fact = int(input())
for _ in range(numeros_fact):
    valorTemp = int(input())
    if 1 <= valorTemp < 20:
        factorialTemp = 1
        for j in range(1, valorTemp + 1):
            factorialTemp *= j
        print(factorialTemp)
