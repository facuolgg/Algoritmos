from list_ import List
from super_heroes_data import superheroes
from queue_ import Queue
from copy import deepcopy


def heroes_to_list(superheroes):
    hero_list = List()
    for hero in superheroes:
        hero_list.append(hero)
    return hero_list

hero_list = heroes_to_list(superheroes)

def criterio_nombre(hero):
    return hero['name']

hero_list.add_criterion('name', criterio_nombre)

hero_list.sort_by_criterion('name')

print("--------------------------------")

print("Listado de personajes ordenados por nombre:")
for hero in hero_list:
    print(hero['name'])

print("--------------------------------")

the_thing_position = hero_list.search('The Thing', 'name')
if the_thing_position is not None:
    print(f'The Thing se encuentra en la posición: {the_thing_position}')
else:
    print('The Thing no se encuentra en la lista')

print("--------------------------------")

rocket_raccoon_position = hero_list.search('Rocket Raccoon', 'name')
if rocket_raccoon_position is not None:
    print(f'Rocket Raccoon se encuentra en la posición: {rocket_raccoon_position}')
else:
    print('Rocket Raccoon no se encuentra en la lista')

print("--------------------------------")

print("Listado de personajes que son villanos:")
for hero in hero_list:
    if hero.get('is_villain') == True:
        print(hero['name'])

print("--------------------------------")

def queue_villains(hero_list):
    villain_queue = Queue()
    for hero in hero_list:
        if hero.get('is_villain') == True:
            villain_queue.arrive(hero)
    return villain_queue

villain_queue = queue_villains(hero_list)

def villains_before_1980(villain_queue):
    while villain_queue.size() > 0:
        villain = villain_queue.attention()
        if villain.get('first_appearance') and int(villain['first_appearance']) < 1980:
            print(villain['name'])
        
print("Villanos que aparecieron antes de 1980:")
villains_before_1980(villain_queue)

print("--------------------------------")

def heroes_starting_with_Bl(hero_list):
    buscado = False
    for hero in hero_list:
        if (hero['name'][:2] == 'Bl') and (hero['is_villain'] == False):
            print(hero['name'])
            buscado = True
    if not buscado:
        print("No se encontraron superhéroes que comiencen con Bl")

print("Listado de superhéroes que comienzan con Bl:")
heroes_starting_with_Bl(hero_list)

print()

def heroes_starting_with_G(hero_list):
    buscado = False
    for hero in hero_list:
        if (hero['name'][0] == 'G') and (hero['is_villain'] == False):
            print(hero['name'])
            buscado = True
    if not buscado:
        print("No se encontraron superhéroes que comiencen con G")
print("Listado de superhéroes que comienzan con G:")
heroes_starting_with_G(hero_list)

print()

def heroes_starting_with_My(hero_list):
    buscado = False
    for hero in hero_list:
        if (hero['name'][:2] == 'My') and (hero['is_villain'] == False):
            print(hero['name'])
            buscado = True
    if not buscado:
        print("No se encontraron superhéroes que comiencen con My")

print("Listado de superhéroes que comienzan con My:")
heroes_starting_with_My(hero_list)

print()

def heroes_starting_with_W(hero_list):
    buscado = False
    for hero in hero_list:
        if (hero['name'][0] == 'W') and (hero['is_villain'] == False):
            print(hero['name'])
            buscado = True
    if not buscado:
        print("No se encontraron superhéroes que comiencen con W")

print("Listado de superhéroes que comienzan con W:")
heroes_starting_with_W(hero_list)

print("--------------------------------")

def criterio_real_name(hero):
    return hero.get('real_name') or ''

hero_list.add_criterion('real_name', criterio_real_name)

hero_list.sort_by_criterion('real_name')

print("Listado de personajes ordenados por su nombre real:")
for hero in hero_list:
    print(hero['real_name'])

print("--------------------------------")

def criterio_first_appearance(hero):
    return hero.get('first_appearance') or 0

hero_list.add_criterion('first_appearance', criterio_first_appearance)

hero_list.sort_by_criterion('first_appearance')

print("Listado de personajes ordenados por su fecha de aparición:")
for hero in hero_list:
    print(hero['name'])


print("--------------------------------")

print("Cambiando el nombre real de Ant Man de Hank Pyma Scott Lang...")
def cambiar_nombre_antman(hero_list):
    for hero in hero_list:
        if hero['name'] == "Ant Man":
            hero['real_name'] = "Scott Lang"

cambiar_nombre_antman(hero_list)

for hero in hero_list:
    if hero['name'] == "Ant Man":
        print(f"El nombre real de {hero['name']} es {hero['real_name']}")

print("--------------------------------")

print("Personajes que incluyen 'time-traveling' o 'suit' en su biografía:")
def mostrar_personajes_time_traveling_o_suit(hero_list):
    buscado = False
    for hero in hero_list:
        biography = hero.get('short_bio', '').lower()
        if 'time-traveling' in biography or 'suit' in biography:
            print(hero['name'])
            buscado = True
    if not buscado:
        print("No se encontraron personajes que incluyan 'time-traveling' o 'suit' en su biografía.")

mostrar_personajes_time_traveling_o_suit(hero_list)

print("--------------------------------")

print("Eliminamos a Electro y Baron Zemo de la lista de personajes si es que se encuentran en ella: ")

def eliminar_personajes(hero_list):
    buscado1 = False
    buscado2 = False
    hero_list_aux = deepcopy(hero_list)
    for hero in hero_list_aux:
        if hero['name'] == "Electro":
            print(f"Eliminando a {hero['name']} de la lista.")
            print(f"Información de {hero['name']}: {hero}")
            hero_list.delete_value(hero['name'], 'name')
            buscado1 = True
        if hero['name'] == "Baron Zemo":
            print(f"Eliminando a {hero['name']} de la lista.")
            print(f"Información de {hero['name']}: {hero}")
            hero_list.delete_value(hero['name'], 'name')
            buscado2 = True
    if not buscado1:
        print("No se encontro a Electro en la lista.")
    if not buscado2:
        print("No se encontro a Baron Zemo en la lista.")

eliminar_personajes(hero_list)