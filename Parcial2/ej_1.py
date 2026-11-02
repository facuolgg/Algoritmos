from pokemon_data import pokemons
from tree import BinaryTree

class Pokemon:
    def __init__(self, d):
        self.nombre = d["nombre"]
        self.numero = d["numero"]
        self.tipos = d["tipos"]
        self.debilidades = d["debilidades"]
        self.tiene_mega = d["tieneMega"]
        self.tiene_gigamax = d["tieneGigamax"]

    def __str__(self):
        return (f"#{self.numero} {self.nombre} | Tipos: {'/'.join(self.tipos)} "
                f"| Debilidades: {'/'.join(self.debilidades)} "
                f"| Mega: {self.tiene_mega} | Gigamax: {self.tiene_gigamax}")

arbol_numero = BinaryTree()
arbol_nombre = BinaryTree()
arbol_tipo = BinaryTree()

# A
for pokemon in pokemons:
    arbol_numero.insert_node(pokemon['numero'], other_value=pokemon)
    arbol_nombre.insert_node(pokemon['nombre'], other_value=pokemon)
    for tipo in pokemon['tipos']:
        arbol_tipo.insert_node(tipo, other_value=pokemon)

# B
def mostrar_por_numero(numero):
    nodo = arbol_numero.search(numero)
    if nodo is not None:
        p = nodo.other_values
        print(f"#{p['numero']} {p['nombre']} | "
              f"Tipos: {'/'.join(p['tipos'])} | "
              f"Debilidades: {'/'.join(p['debilidades'])} | "
              f"Mega: {p['tieneMega']} | Gigamax: {p['tieneGigamax']}")
    else:
        print(f"No existe Pokémon con número {numero}")


print("Búsqueda por número:")
num_str = input("Ingrese el número del Pokémon que desea buscar: ")
try:
    num = int(num_str)
    mostrar_por_numero(num)
except ValueError:
    print(f"   '{num_str}' no es un número válido.")
print("-" * 60)

print("Búsqueda por proximidad en el nombre")
search_str = input("Ingrese lo que quiere buscar: ")
arbol_nombre.proxy_search(search_str.lower())

def mostrar_completo_por_proximidad(subcadena):
    def __por_proxy(root, sub):
        if root is None:
            return
        __por_proxy(root.left, sub)
        if sub in root.value.lower():
            p = root.other_values
            print(f"  #{p['numero']} {p['nombre']} | "
                  f"Tipos: {'/'.join(p['tipos'])} | "
                  f"Debilidades: {'/'.join(p['debilidades'])} | "
                  f"Mega: {p['tieneMega']} | Gigamax: {p['tieneGigamax']}")
        __por_proxy(root.right, sub)
    __por_proxy(arbol_nombre.root, subcadena.lower())

print("Datos completos de los Pokémon encontrados:")
mostrar_completo_por_proximidad(search_str)
print("-" * 60)

# C
def nombres_por_tipo(tipo):
    print(f"Pokémon de tipo {tipo}:")
    encontrados = 0

    def __por_tipo(root, sub):
        nonlocal encontrados
        if root is None:
            return
        __por_tipo(root.left, sub)
        if root.value == tipo:
            print(f"  - {root.other_values['nombre']}")
            encontrados += 1
        __por_tipo(root.right, sub)

    __por_tipo(arbol_tipo.root, tipo)
    if encontrados == 0:
        print("  (ninguno)")


print("Nombres por tipo:")
for t in ['Fantasma', 'Fuego', 'Acero', 'Eléctrico']:
    nombres_por_tipo(t)
    print()
print("-" * 60)

# D
def inorden_por_numero_y_nombre(arbol):
    def __inorden(root):
        if root is None:
            return
        __inorden(root.left)
        p = root.other_values
        print(f"  #{p['numero']} {p['nombre']}")
        __inorden(root.right)
    __inorden(arbol.root)

print("Listado en orden ascendente por número: ")
inorden_por_numero_y_nombre(arbol_numero)

print("Listado en orden ascendente por nombre: ")
inorden_por_numero_y_nombre(arbol_nombre)

print("Listado por nivel por nombre: ")
arbol_nombre.by_level()
print("-" * 60)

# E
def debiles_frente_a(pokemon_nombre):
    print(f"Pokémon débiles frente a {pokemon_nombre}:")
    debilidades = set()
    for p in pokemons:
        if p['nombre'].lower() == pokemon_nombre.lower():
            debilidades = set(p['debilidades'])
            break
    if not debilidades:
        print(f"  No se encontró el Pokémon {pokemon_nombre}.")
        return

    encontrados = 0
    for p in pokemons:
        if any(tipo in debilidades for tipo in p['tipos']):
            print(f"  - {p['nombre']}")
            encontrados += 1
    if encontrados == 0:
        print("  (ninguno)")

for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    debiles_frente_a(nombre)
    print()
print("-" * 60)

# F
def mostrar_tipos_y_cantidad():
    tipo_cantidad = {}
    for p in pokemons:
        for tipo in p["tipos"]:
            if tipo in tipo_cantidad:
                tipo_cantidad[tipo] += 1
            else:
                tipo_cantidad[tipo] = 1
    for tipo, cantidad in tipo_cantidad.items():
        print(f"- {tipo}: {cantidad}")

print("Tipos de pokemon y cantidad: ")
mostrar_tipos_y_cantidad()
print("-" * 60)

# G
def contar_megaevolucion():
    mega_count = 0
    for p in pokemons:
        if p["tieneMega"]:
            mega_count += 1
    return mega_count

print("Cantidad de pokemon con megaevolución: ", contar_megaevolucion())
print("-" * 60)

# H
def contar_gigamax():
    gigamax_count = 0
    for p in pokemons:
        if p["tieneGigamax"]:
            gigamax_count += 1
    return gigamax_count

print("Cantidad de pokemon con gigamax: ", contar_gigamax())

