#sintax (llave, valor)
from this import d

dicc={
    "HDP":"Hijo de la procrastinacion",
    "PATMQTHLT":"Pidele a tu mama que te haga la tarea",
    "Aaron": "Cholo"

}
print(dicc)

print(len(dicc))

#acceder con la llave
print(dicc["Aaron"])
#no se puede
# print(dicc[1])
#acceder con la llave
print(dicc.get("Aaron"))

#modifi value
dicc["Aaron"]="Delincuente"
print(dicc)
#ver todos lo elementos con el for llave y su significado
for abv, signi  in dicc.items():
    print(f"Esta el término {abv} y significa {signi}")

#ver todas las llave 
for abv in dicc:
    print(f"Esta el término {abv}")
for termino in dicc.keys():
    print(f"Esta el término {termino}")


#ver todos los valores o significados
for sig in dicc.values():
    print(f"Esta la definicion {sig}")


#ver si existe una cosa
print("Mojang" in dicc)

#agregar
dicc["Mojang"]="Una cosa"
print(dicc)

#quitar
# dicc.pop("HDP")
print(dicc)
#actualizar(agreganfdo)
dicc.update({"Chuek":"Dios"})
print(dicc)
#Quitar dicc
#del dicc


#------------Practica 2

puntajes={"Shrek": 500,"Shaggy": 1000, "Juan Leonidas": 600, "PElon dante": 550}
calificacion={}


for n in puntajes.keys():
    puntaje=puntajes[n]
    if puntaje>900:
        calificacion[n]=f"Explosivo {puntaje}"
    elif puntaje>599:
        calificacion[n]=f"Normal {puntaje}"
    elif puntaje>499:
        calificacion[n]=f"silencioso {puntaje}"
    
print(calificacion)

#-----------Combinar listas y Dicc
capitales={"Francia":"PAris", "Alemania":"Berlin", "Mexico":"CDMX", "USA":"Washington"}
ciudades={"Francia": ["paris", "monte carlo xd "],  "Alemania": ["Berlin", "Orangenschaft xd "]}
#-----------Dicc+Dicc
viajes={"Francia":{"pending":["paris", "monte carlo xd "], "Visited":[]}}
#DICCS en listas

viajes2=[
    {"Francia":
    {"pending":["paris", "monte carlo xd "], 
    "Visited":0}
    }, 
    {"Alemania":
    {"pending":["Berlin", "SSchawrz"], 
    "Visited":0}
    }
]
def add_country(pais, pendientes, visitados):
    nuevo_pais={}
    nuevo_pais["pais"]=pais
    nuevo_pais["pendientes"]=pendientes
    nuevo_pais["visitados"]=visitados
    viajes2.append(nuevo_pais)
    print(viajes2)
add_country("Russia", ["Moscow", "San petesburgo"],1)




order = {
    "starter": {"XD": "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"])#imprime el dicc main
print(order["main"][2]) #imprime el valor de el segundo termino con []
print(order["main"][2][0])# imprime el valor Steak
print(order["starter"]["XD"])


