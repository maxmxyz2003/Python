for i in range(6):
    if i%2==0:
        print(f"Valor {i}")
    else:
        print("Valor impar {i}")


#Con el continue se omite el valor con la condicion

for i in range(11):
    if i%2==1:
        continue
    else:
        print(f"Valor par {i}")


for i in range(12):
    if i%2==0:
        print(f"Valor {i}")
    if i%2==10:
        break
numero="12-3445-67-89"
for i in numero:
    if i=="-":
        continue
    print(i, end="")