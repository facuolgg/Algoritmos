from trainers_pokemon import trainers
from list_ import List

l = List(trainers)

# a) Obtener la cantidad de pokémon de un determinado entrenador.

def cantidad_pokemons_entrenador(l):
    nombre_entrenador = input("Ingrese el nombre del entrenador: ").lower()
    #nombre_entrenador = "brock"
    l.add_criterion("name", lambda x: x["name"])
    index = l.search(nombre_entrenador, "name")
    print(f"Buscando la cantidad de pokémon del entrenador {nombre_entrenador}...")
    if index is not None:
        entrenador = l[index]
        cantidad_pokemons = len(entrenador["pokemons"])
        print(f"El entrenador {nombre_entrenador} tiene {cantidad_pokemons} pokémon.")
    else:
        print(f"El entrenador {nombre_entrenador} no se encuentra en la lista.")

print("\nPunto a) Obtener la cantidad de pokémon de un determinado entrenador")
cantidad_pokemons_entrenador(l)

# b) Listar los entrenadores que hayan ganado más de tres torneos

def mas_tres_torneos(l):
    for element in l:
        if element["tournaments_won"] > 3:
            print(element["name"])

print("\nPunto b) Listar los entrenadores que hayan ganado más de tres torneos")
mas_tres_torneos(l)

# c) El pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados

def mayor_nivel(l):
    mas_torneos = max(l, key= lambda x: x["tournaments_won"])
    mayor_nivel = max(mas_torneos["pokemons"], key= lambda x: x["level"])
    print(f"El entrenador con más torneos ganados es {mas_torneos["name"]} y su pokémon de mayor nivel es {mayor_nivel["name"]}, con nivel {mayor_nivel["level"]}")

print("\nPunto c) El pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados")
mayor_nivel(l)

# d) Mostrar todos los datos de un entrenador y sus Pokémons

def mostrar_datos(l):
    l.add_criterion("name", lambda x: x["name"])
    nombre_entrenador = input("Ingrese el nombre del entrenador que del que desea buscar sus datos: ").lower()
    #nombre_entrenador = "lance"
    index = l.search(nombre_entrenador, "name")
    print(l[index])

print("\nPunto d) Mostrar todos los datos de un entrenador y sus Pokémons")
mostrar_datos(l)

# e) Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%

def batallas_79(l):
    for element in l:
        if element["porcentaje_batallas_ganadas"] > 79:
            print(element["name"])

print("\nPunto e) Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%")
batallas_79(l)

# f) Los entrenadores que tengan Pokémons de tipo fuego o planta, o de agua/volador (tipo y subtipo)

def pokemon_tipo(l):
    print("Los entrenadores que tienen pokémon tipo fuego, planta o agua/volador son: ")
    entrenadores = []
    for element in l:
        for pokemon in element["pokemons"]:
            if (pokemon["type"] == "Fuego" or pokemon["type"] == "Planta")  or (pokemon["type"] == "Agua" and pokemon["subtype"] == "Volador"):
                if element["name"] not in entrenadores:
                    print(element["name"])
                    entrenadores.append(element["name"])


print("\nPunto f) Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador")
pokemon_tipo(l)

# g) El promedio de nivel de los Pokémons de un determinado entrenador

def promedio_nivel(l):
    sumnivel = 0
    nombre_entrenador = input("Ingrese el nombre del entrenador: ").lower()
    #nombre_entrenador = "ash ketchum"
    l.add_criterion("name", lambda x: x["name"])
    index = l.search(nombre_entrenador, "name")
    if index is not None:
        entrenador = l[index]
        cantidad_pokemons = len(entrenador["pokemons"])
        for pokemon in entrenador["pokemons"]:
            sumnivel += pokemon["level"]
        promedio = sumnivel / cantidad_pokemons

    
    print(f"El promedio de nivel de los Pokémon de {nombre_entrenador} es de: {promedio}")

print("\nPunto g) El promedio de nivel de los Pokémons de un determinado entrenador")
promedio_nivel(l)

# h) Determinar cuantos entrenadores tienen a un determinado Pokémon

def cont_entrenadores_segun_pokemon(l):
    entrenadores = []
    buscado = input("Ingrese el pokémon que busca: ")
    #buscado = "Gyarados"
    count = 0
    for element in l:
        for pokemon in element["pokemons"]:
            if (pokemon["name"] == buscado):
                if element["name"] not in entrenadores:
                    count += 1
                    entrenadores.append(element["name"])

    print(f"La cantidad de entrenadores que tienen a {buscado} son: {count}")

print("\nPunto h) Determinar cuantos entrenadores tienen a un determinado Pokémon")
cont_entrenadores_segun_pokemon(l)

# i) Mostrar los entrenadores que tienen pokémons repetidos

def entrenadores_con_pokemons_repetidos(l):
    for entrenador in l:
        vistos = set()
        repetidos = set()

        for pokemon in entrenador["pokemons"]:
            nombre = pokemon["name"]
            if nombre in vistos:
                repetidos.add(nombre)
            vistos.add(nombre)

        if repetidos:
            print(f"{entrenador['name']}: {', '.join(sorted(repetidos))}")

print("\nPunto i) Mostrar los entrenadores que tienen pokémons repetidos")
entrenadores_con_pokemons_repetidos(l)

# j) Determinar los entrenadores que tengan uno de los siguientes pokémons: Tyrantrum, Terrakion o Wingull

def porpokemon(l):
    entrenadores_vistos = []
    for element in l:
        for pokemon in element["pokemons"]:
            if pokemon["name"] == "Tyrantrum":
                print(f'El entrenador {element["name"]} tiene al pokemon Tyrantrum')
                entrenadores_vistos.append(element["name"])
            elif pokemon["name"] == "Terrakion":
                print(f'El entrenador {element["name"]} tiene al pokemon Terrakion')
                entrenadores_vistos.append(element["name"])
            elif pokemon["name"] == "Wingull":
                print(f'El entrenador {element["name"]} tiene al pokemon Wingull')
                entrenadores_vistos.append(element["name"])

print("\nPunto j) Determinar los entrenadores que tengan uno de los siguientes pokémons: Tyrantrum, Terrakion o Wingull")
porpokemon(l)

#k determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos

def buscar_pokemon_por_entrenador(l):
    l.add_criterion("name", lambda x: x["name"])
    entrenador_buscado = input("Ingrese el entrenador que busca: ").lower()
    pokemon_buscado = input("Ingrese el pokémon que busca: ")
    index = l.search(entrenador_buscado, "name")
    entrenador = l[index]
    encontrado = False
    if index is not None:
        for pokemon in entrenador["pokemons"]:
            if (pokemon["name"] == pokemon_buscado):
                print(f"El entrenador {entrenador_buscado} tiene al pokemon {pokemon_buscado}")
                print(f"Información del entrenador: {entrenador}")
                print(f"Información del Pokémon: {pokemon}")
                encontrado = True
                

        if not encontrado:
            print(f"El entrenador {entrenador_buscado} no tiene al pokemon {pokemon_buscado}")


print("\nPunto k) Determinar si un entrenador X tiene un pokemon Y. Si es así, mostrar info.")
buscar_pokemon_por_entrenador(l)
