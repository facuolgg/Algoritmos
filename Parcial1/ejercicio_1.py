from list_ import List
from super_heroes_data import superheroes

def heroes_to_list(superheroes):
    hero_list = List()
    for hero in superheroes:
        hero_list.append(hero)
    return hero_list

hero_list = heroes_to_list(superheroes)

def cap_en_lista(hero_list, indice=0):
    if indice >= len(hero_list):
        print('Capitan America no se encuentra en la lista')
        return False
    if hero_list[indice]['name'] == 'Captain America':
        print('Capitan America se encuentra en la lista')
        return True
    return cap_en_lista(hero_list, indice + 1)

cap_en_lista(hero_list, 0)

def listar_heroes(hero_list, indice=0):
    if indice >= len(hero_list):
        return
    print(hero_list[indice]['name'])
    listar_heroes(hero_list, indice + 1)

listar_heroes(hero_list)

