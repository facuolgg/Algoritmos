from queue_ import Queue
from copy import deepcopy

queue = Queue()

def personaje(queue, nombre, sup, gen):
    queue.arrive((nombre, sup, gen))

personaje(queue, "Tony Stark", "Iron Man", "M")
personaje(queue, "Steve Rogers", "Capitan America", "M")
personaje(queue, "Natasha Romanoff", "Black Widow", "F")
personaje(queue, "Scott Lang", "Ant-Man", "M")
personaje(queue, "Carol Danvers", "Capitana Marvel", "F")
personaje(queue, "Peter Parker", "Spider-Man", "M")

def det_nombre (queue):
    queue_aux1 = Queue()
    queue_aux1 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux1.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux1.attention()
            if sup_aux == "Capitana Marvel":
                print(f"El nombre de Capitana Marvel es {nombre_aux}")
                buscado = True
        if not buscado:
            print("No se encontró a Capitana Marvel en la cola")
    else:
        print("No hay personajes en la cola")

print("-----------------------------------------------")
det_nombre(queue)

def femeninos(queue):
    queue_aux2 = Queue()
    queue_aux2 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux2.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux2.attention()
            if gen_aux == "F":
                print(f"El nombre de {sup_aux} es {nombre_aux}")
                buscado = True
        if not buscado:
            print("No se encontraron personajes femeninos en la cola")
    else:
        print("No hay personajes en la cola")

print("-----------------------------------------------")
print(f"Los personajes de genero femenino son: {femeninos(queue)}")

def masculinos(queue):
    queue_aux3 = Queue()
    queue_aux3 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux3.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux3.attention()
            if gen_aux == "M":
                print(f"El nombre de {sup_aux} es {nombre_aux}")
                buscado = True
        if not buscado:
            print("No se encontraron personajes masculinos en la cola")
    else:
        print("No hay personajes en la cola")

print("-----------------------------------------------")
print(f"Los personajes de genero masculino son: {masculinos(queue)}")

def det_sup (queue):
    queue_aux4 = Queue()
    queue_aux4 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux4.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux4.attention()
            if nombre_aux == "Scott Lang":
                print(f"El nombre de Ant-Man es {nombre_aux}")
                buscado = True
        if not buscado:
            print("No se encontró a Ant-Man en la cola")
    else:
        print("No hay personajes en la cola")

print("-----------------------------------------------")
det_sup(queue)

def nombres_s(queue):
    queue_aux5 = Queue()
    queue_aux5 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux5.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux5.attention()
            if (sup_aux[0] == "S"):
                print(f"{sup_aux} es un superheroe cuyo nombre empieza con S, sus datos son: Nombre: {nombre_aux}, Género: {gen_aux}")
                buscado = True
            elif (nombre_aux[0] == "S"):
                print(f"{nombre_aux} es un personaje cuyo nombre empieza con S, sus datos son: Nombre: {nombre_aux}, Género: {gen_aux}")
                buscado = True
        if not buscado:
            print("No se encontraron personajes cuyo nombre empiece con S")
    else:
        print("No hay personajes en la cola")

print("-----------------------------------------------")
nombres_s(queue)

def danvers (queue):
    queue_aux6 = Queue()
    queue_aux6 = deepcopy(queue)
    buscado = False
    if queue.size() > 0:
        while queue_aux6.size() > 0:
            nombre_aux, sup_aux, gen_aux = queue_aux6.attention()
            if nombre_aux == "Carol Danvers":
                print(f"Carol Danvers se encuentra en la cola y su nombre de superheroe es {sup_aux}")
                buscado = True
        if not buscado:
            print("No se encontró a Carol Danvers en la cola")
    else:
        print("No hay personajes en la cola")
    
print("-----------------------------------------------")
danvers(queue)