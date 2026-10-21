num1 = int(input())
operador = input().strip()
num2 = int(input())

if num2 == 0 and operador in ['/', '%']:
    print("indefinido")
else:
    if operador == '%':
        result = num1 % num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '/':
        result = num1 // num2
    
    print(result)
