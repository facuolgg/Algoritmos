from criaturas_data import creatures
from tree import BinaryTree
from queue_ import Queue

class Creature():

    def __init__(self, name, defeated_by, capturada=None, descripcion=""):
        self.name = name
        self.defeated_by = defeated_by
        self.capturada = capturada
        self.descripcion = descripcion


    def __str__(self):
        return f"{self.name} - Derrotado por: {self.defeated_by} - Capturada por: {self.capturada} - Descripción: {self.descripcion}"


creature_tree = BinaryTree()

for c in creatures:
    new_creature = Creature(
        name=c["name"], 
        defeated_by=c["defeated_by"],
        capturada=None,
        descripcion=""
    )
    creature_tree.insert_node(new_creature.name, other_value=new_creature)

# A 
def inorder_nodes(node):
    if node is not None:
        yield from inorder_nodes(node.left)
        yield node
        yield from inorder_nodes(node.right)

inorder_nodes(creature_tree)

def list_creatures(tree):
    for node in inorder_nodes(tree.root):
        defeated_by = node.other_values.defeated_by or "-"
        print(f'{node.value} - derrotado por: {defeated_by}')

list_creatures(creature_tree)
print("-" * 60)

# B
def cargar_descripcion(tree):
    while True:
        nombre = input("Ingrese el nombre de la criatura (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
            
        node = tree.search(nombre)
        if node is not None:
            if node.other_values.descripcion:
                print(f"Ya tiene descripción: {node.other_values.descripcion}")
                if input("¿Sobrescribir? (s/n): ").lower() != 's':
                    continue
            
            desc = input(f"Ingrese descripción para {nombre}: ")
            node.other_values.descripcion = desc 
            print(f"Descripción cargada para {nombre}.")
        else:
            print(f"No se encontró '{nombre}'.")

cargar_descripcion(creature_tree)
print("-" * 60)
# Método para verificar si se cargaron las descripciones
def verificar_descripciones(tree):
    for node in inorder_nodes(tree.root):
        criatura = node.other_values
        if criatura.descripcion:
            print(f"[✓] {criatura.name}: {criatura.descripcion}")
        else:
            print(f"[ ] {criatura.name}: (sin descripción)")
    
#verificar_descripciones(creature_tree)
#print("-" * 60)

# C
print("Datos de la Talos: ")
buscado = creature_tree.search("Talos")
if buscado is not None:
    data = buscado.other_values
    print(f"Nombre: {data.name}")
    print(f"Derrotado por: {data.defeated_by}")
    print(f"Capturada por: {data.capturada}")
    print(f"Descripción: {data.descripcion}")
else:
    print("No se encontró la criatura 'Talos'.")
print("-" * 60)

# D
def top_3_heroes(tree):
    victorias = {}
    for node in inorder_nodes(tree.root):
        heroe = node.other_values.defeated_by
        if heroe is not None:
            victorias[heroe] = victorias.get(heroe, 0) + 1

    ranking = sorted(victorias.items(), key=lambda x: x[1], reverse=True)

    print("Ranking de Héroes:")
    for i, (heroe, cantidad) in enumerate(ranking[:3], 1):
        print(f"{i}. {heroe} - {cantidad} criaturas derrotadas")

top_3_heroes(creature_tree)
print("-" * 60)

# E
def defeated_creatures(tree, hero_name):
    print(f"Criaturas derrotadas por {hero_name}:")
    for node in inorder_nodes(tree.root):
        if node.other_values.defeated_by == hero_name:
            print(f"- {node.value}")

defeated_creatures(creature_tree, "Heracles")
print("-" * 60)

# F
def not_defeated(tree):
    for node in inorder_nodes(tree.root):
        if node.other_values.defeated_by == None:
            print(f"- {node.value}")

print("Criaturas no derrotadas: ")
not_defeated(creature_tree)
print("-" * 60)

# H
creatures_heracles = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

def modify_capture_heracles(tree):
    for creature in creatures_heracles:
        node = tree.search(creature)
        if node is not None:
            node.other_values.capturada = "Heracles"
        else:
            print(f"No se encontró la criatura '{creature}'.")

modify_capture_heracles(creature_tree)
print("Capturas de Heracles cargadas.")

buscados = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

# # Para verificar si se cargaron las capturas
# for buscado in buscados:
#     node = creature_tree.search(buscado)
#     if node is not None:
#         data = node.other_values
#         print(f"Nombre: {data.name}")
#         print(f"Derrotado por: {data.defeated_by}")
#         print(f"Capturada por: {data.capturada}")
#         print(f"Descripción: {data.descripcion}")
#         print("----------------------------------------------")
#     else:
#         print(f"No se encontró la criatura '{buscado}'.")
#         print("----------------------------------------------")
print("-" * 60)

# I
search_str = input("Ingrese el texto que quiere buscar: ")
creature_tree.proxy_search(search_str)

# J 
def delete_creature(tree):
    borrar = ["Basilisco", "Sirenas"]
    for nombre in borrar:
        node = tree.search(nombre)
        if node is not None:
            tree.delete_node(nombre)
        else:
            print(f"No se encontró la criatura '{nombre}' para eliminar.")

delete_creature(creature_tree)
print("-" * 60)

# K
node_aves = creature_tree.search("Aves del Estínfalo")
if node_aves is not None:
    node_aves.other_values.defeated_by = "Varias fueron derrotadas por Heracles"
else:
    print("No se encontraron las Aves del Estínfalo.")

# L
node_dragon = creature_tree.search("Ladón")
if node_dragon is not None:
    objeto_ladon = node_dragon.other_values
    creature_tree.delete_node("Ladón")
    objeto_ladon.name = "Dragón Ladón"
    creature_tree.insert_node(objeto_ladon.name, other_value=objeto_ladon)
else:
    print("No se encontró el Ladón.")

list_creatures(creature_tree)
print("-" * 60)

# M
creature_tree.by_level()
print("-" * 60)

# N
def captured_creatures(tree, hero_name):
    print(f"Criaturas capturadas por {hero_name}:")
    for node in inorder_nodes(tree.root):
        if node.other_values.capturada == hero_name:
            print(f"- {node.value}")

captured_creatures(creature_tree, "Heracles")
# Heracles capturó varias Aves del Estínfalo, pero no está cargado como capturador de ellas pues no las capturó a todas.
print("-" * 60)


