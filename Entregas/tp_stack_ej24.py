from stack import Stack
from copy import copy, deepcopy

pila = Stack()

def personaje(pila, nombre, pelis):
    pila.push((nombre, pelis))

def posicion(pila):
    pila_aux = Stack()
    pila_aux = deepcopy(pila)
    if pila.size() > 0:
        while pila_aux.size() > 0:
            nombre_aux, pelis_aux = pila_aux.pop()
            if nombre_aux == "Rocket Raccoon" or nombre_aux == "Groot":
                print(f"{nombre_aux} se encuentra en la posición {pila.size() - pila_aux.size()} de la pila")
    else:
        print("No hay personajes en la pila")

def cant_pelis(pila):
    count = 0
    pila_aux2 = Stack()
    pila_aux2 = deepcopy(pila)
    if pila.size() > 0:
        while pila_aux2.size() > 0:
            nombre_aux, pelis_aux = pila_aux2.pop()
            if pelis_aux >= 5:
                print(f"{nombre_aux} ha participado en {pelis_aux} películas")
                count += 1
    else:
        print("No hay personajes en la pila")
    return count

def black_widow(pila):
    pila_aux3 = Stack()
    pila_aux3 = deepcopy(pila)
    if pila.size() > 0:
        while pila_aux3.size() > 0:
            nombre_aux, pelis_aux = pila_aux3.pop()
            if nombre_aux == "Black Widow":
                print(f"{nombre_aux} ha participado en {pelis_aux} películas")
    else:
        print("No hay personajes en la pila")
   
def nombres_cdg(pila):
    pila_aux4 = Stack()
    pila_aux4 = deepcopy(pila)
    if pila.size() > 0:
        while pila_aux4.size() > 0:
            nombre_aux, pelis_aux = pila_aux4.pop()
            if nombre_aux[0] == "C":
                print(f"{nombre_aux} es un personaje cuyo nombre empieza con C")
            elif nombre_aux[0]== "D":
                print(f"{nombre_aux} es un personaje cuyo nombre empieza con D")
            elif nombre_aux[0] == "G":
                print(f"{nombre_aux} es un personaje cuyo nombre empieza con G")
            
    else:
        print("No hay personajes en la pila")

# PRUEBA (la cantidad de peliculas no es la real)
personaje(pila, "Groot", 4)
personaje(pila, "Black Widow", 6)
personaje(pila, "Rocket Raccoon", 4)
personaje(pila, "Star-Lord", 4)
personaje(pila, "Capitan América", 7)
personaje(pila, "Doctor Strange", 5)

pila.show()

print("------------------------")

posicion(pila)

print("------------------------")

cant_pelis(pila)

print("------------------------")

black_widow(pila)

print("------------------------")

nombres_cdg(pila)
