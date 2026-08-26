print("HOLA bienbenu al creador de bandas 3000")

zx=input("Escribe una ciudad: ")
vxd=input("Escribe un nombre random: ")
nombre=zx+vxd
with open("databandas.txt", "a") as data:
    data.write(f"{nombre}\n")

print(nombre)