#no tiene orden ni duplicados
planetas={"marte", "Jupiter", "venus"}
print(planetas)

#cant de elmentos
print(len(planetas))
#revisar si hay iun valor
print("marte" in planetas)
print("Calamardo" in planetas)
#incluir elemento
planetas.add("Calamard0")
print(planetas)

#excluir elemento
planetas.discard("Calamard0")
print(planetas)
#---------------
animales={"vaca", "toro", "caballo", "cerdo"}
carne={"vaca", "cerdo", "atún"}
#Comparar
print(animales.difference(carne))

#unir
print(animales.union(carne))

#eliminare 
#del planetas