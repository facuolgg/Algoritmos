
from super_heroes_data import superheroes
from tree import BinaryTree

class MarvelCharacter():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"
    


arbol_marvel = BinaryTree()

#print(f'cantidad de elementos {len(superheroes)}')
# #A
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)
print("Los personajes de marvel se han insertado correctamente en el árbol binario.")
print("-" * 50)

# #B
print("La lista de villanos ordenada alfabeticamente es: ")
arbol_marvel.inorden_villain()
print("-" * 50)

# #C
print("Los heroes que comienzan con la letra C son los siguientes: ")
arbol_marvel.inorden_hero_star_with('C')
print("-" * 50)

# #D
print(f'Cantidad de heroes en el arbol: {arbol_marvel.count_heroes()}')

# #E
search_str = input('ingrese lo que quiere buscar: ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar: ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)

print("-" * 50)
print("Lista actualizada: ")
arbol_marvel.inorden_hero_star_with('D')

# #F
arbol_marvel.postorden_hero()

# #G
arbol_heroes = BinaryTree()
arbol_villains = BinaryTree()

def separar_personajes(nodo):
    if nodo is None:
        return

    if nodo.other_values['is_villain']:
        arbol_villains.insert_node(nodo.value, nodo.other_values)
    else:
        arbol_heroes.insert_node(nodo.value, nodo.other_values)

    separar_personajes(nodo.left)
    separar_personajes(nodo.right)


def count_nodes(nodo):
    if nodo is None:
        return 0
    return 1 + count_nodes(nodo.left) + count_nodes(nodo.right)

separar_personajes(arbol_marvel.root)

print(f"Cantidad de nodos en arbol_heroes: {count_nodes(arbol_heroes.root)}")
print("-" * 50)
print(f"Cantidad de nodos en arbol_villains: {count_nodes(arbol_villains.root)}")
print("-" * 50)
print("Barrido ordenado alfabeticamente de arbol_heroes:")
arbol_heroes.inorden()

print("-" * 50)

print("Barrido ordenado alfabeticamente de arbol_villains:")
arbol_villains.inorden()


