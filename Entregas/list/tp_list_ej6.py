from super_heroes import superheroes
from list_ import List
from copy import deepcopy

# a) Eliminar el nodo que contiene la información de "Linterna Verde"
l = List(superheroes)

def eliminar_linterna_verde(l):
    l_aux = deepcopy(l)
    print("Lista de superhéroes antes de eliminar a Linterna Verde:")
    l_aux.show()
    print("-" * 50)
    print("Eliminando Linterna Verde...")
    l_aux.add_criterion("alias", lambda x: x["alias"])
    l_aux.delete_value("Linterna Verde", "alias")
    print("-" * 50)
    print("Lista de superhéroes después de eliminar a Linterna Verde:")
    l_aux.show()

print("\nPunto a) Eliminar el nodo que contiene la información de 'Linterna Verde'")
eliminar_linterna_verde(l)


# b) Mostrar el año de aparición de "Wolverine"

def mostrar_aparicion_wolverine(l):
    l.add_criterion("name", lambda x: x["name"])
    index = l.search("Wolverine", "name")
    if index is not None:
        wolverine = l[index]
        print(f"El año de aparición de Wolverine es: {wolverine['first_appearance']}")
    else:
        print("Wolverine no se encuentra en la lista.")

print("-" * 50)
print("\nPunto b) Mostrar el año de aparición de 'Wolverine'")
mostrar_aparicion_wolverine(l)

# c) Cambiar la casa de Dr Strange a Marvel

def cambiar_casa_dr_strange(l):
    l.add_criterion("name", lambda x: x["name"])
    index = l.search("Doctor Strange", "name")
    if index is not None:
        dr_strange = l[index]
        print(f"La casa actual de Doctor Strange es {dr_strange['house']}")
        dr_strange['house'] = "Marvel"
        print(f"La casa de Doctor Strange ha sido cambiada a {dr_strange['house']}")
    else:
        print("Doctor Strange no se encuentra en la lista.")

print("-" * 50)
print("\nPunto c) Cambiar la casa de 'Doctor Strange' a 'Marvel'")
cambiar_casa_dr_strange(l)

# d) Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra "traje" o "armadura"

def mostrar_superheroes_con_traje_o_armadura(l):
    print("Superhéroes que mencionan 'traje' o 'armadura' en su biografía:")
    l.filter_contain_on_bio(["traje", "armadura"])

print("-" * 50)
print("\nPunto d) Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra 'traje' o 'armadura'")
mostrar_superheroes_con_traje_o_armadura(l)

# e) Mostrar el nombre y la casa de aquellos superhéroes cuya fecha de aparición sea anterior a 1963

def mostrar_superheroes_antes_de_1963(l):
    print("Lista de superhéroes cuya fecha de aparición es anterior a 1963: ")
    for element in l:
        if element['first_appearance'] < 1963:
            print(f"Nombre: {element['name']}, Casa: {element['house']}")

print("-" * 50)
print("\nPunto e) Mostrar el nombre y la casa de aquellos superhéroes cuya fecha de aparición sea anterior a 1963")
mostrar_superheroes_antes_de_1963(l)

# f) Mostrar la casa a la que  pertenece Capitana Marvel y Mujer Maravilla

def mostrar_casa_capitana_mujer_maravilla(l):
    l.add_criterion("name", lambda x: x["name"])
    index_capitana = l.search("Capitana Marvel", "name")
    index_mujer = l.search("Mujer Maravilla", "name")
    print(f"Capitana Marvel pertenece a la casa {l[index_capitana]['house']}")
    print(f"Mujer Maravilla pertenece a la casa {l[index_mujer]['house']}")

print("-" * 50)
print("\nPunto f) Mostrar la casa a la que pertenece 'Capitana Marvel' y 'Mujer Maravilla'")
mostrar_casa_capitana_mujer_maravilla(l)

# g) Mostrar toda la información de Flash y Star-Lord

def mostrar_info_flash_star_lord(l):
    l.add_criterion("name", lambda x: x["name"])
    index_flash = l.search("Flash", "name")
    index_star_lord = l.search("Star-Lord", "name")
    print(f"Información de Flash: {l[index_flash]}")
    print(f"Información de Star-Lord: {l[index_star_lord]}")

print("-" * 50)
print("\nPunto g) Mostrar toda la información de 'Flash' y 'Star-Lord'")
mostrar_info_flash_star_lord(l)

# h) Listar los superhéroes que comiencen con la letra B, M y S

def listar_superheroes_por_letra(l):
    print("Superhéroes que comienzan con la letra B:")
    l.filter_start_with("B")
    print("\nSuperhéroes que comienzan con la letra M:")
    l.filter_start_with("M")
    print("\nSuperhéroes que comienzan con la letra S:")
    l.filter_start_with("S")

print("-" * 50)
print("\nPunto h) Listar los superhéroes que comiencen con la letra B, M y S")
listar_superheroes_por_letra(l)

# i) Determinar la cantidad de superhéroes que hay en cada casa

def contar_superheroes_por_casa(l):
    count_marvel = 0
    count_dc = 0
    for element in l:
        if element['house'] == "Marvel":
            count_marvel += 1
        elif element['house'] == "DC":
            count_dc += 1
    print(f"Cantidad de superhéroes en Marvel: {count_marvel}")
    print(f"Cantidad de superhéroes en DC: {count_dc}")

print("-" * 50)
print("\nPunto i) Determinar la cantidad de superhéroes que hay en cada casa")
contar_superheroes_por_casa(l)