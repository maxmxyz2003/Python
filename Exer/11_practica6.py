nombre=str(input("Escribe el nombre del libro: "))
identifier=int(input("Escribe el ID del libro: "))
precio=float(input("Escribe el precio: "))
envio=input("Tiene envio gratis? (True/False): ")

if envio=="True":
  envio=True
elif envio=="False":
  envio=False


print(f"Nombre del libro: {nombre}")
print(f"ID del libro: {identifier}")
print(f"PRecio y cuanto cuesta el libro: {precio}")
print(f"Envio gratis (True/False): {envio}")