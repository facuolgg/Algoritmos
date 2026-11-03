from graph import Graph

g = Graph(is_dir=False)

nodos = {
    'Router 1': {'tipo': 'router'}, 'Router 2': {'tipo': 'router'}, 'Router 3': {'tipo': 'router'},
    'Switch 1': {'tipo': 'switch'}, 'Switch 2': {'tipo': 'switch'},
    'Red Hat': {'tipo': 'notebook'}, 'Debian': {'tipo': 'notebook'}, 'Arch': {'tipo': 'notebook'},
    'Manjaro': {'tipo': 'pc'}, 'Ubuntu': {'tipo': 'pc'}, 'Mint': {'tipo': 'pc'}, 'Fedora': {'tipo': 'pc'},
    'Guarani': {'tipo': 'servidor'}, 'MongoDB': {'tipo': 'servidor'},
    'Impresora': {'tipo': 'impresora'}
}

for name, info in nodos.items():
    g.add_vertex(name, info)

grafo = {
    'Switch 1': {'Debian': 17, 'Ubuntu': 18, 'Impresora': 22, 'Mint': 80, 'Router 1': 29},
    'Debian': {'Switch 1': 17},
    'Ubuntu': {'Switch 1': 18},
    'Impresora': {'Switch 1': 22},
    'Mint': {'Switch 1': 80},
    'Router 1': {'Switch 1': 29, 'Router 2': 37, 'Router 3': 43},
    'Router 2': {'Router 1': 37, 'Red Hat': 25, 'Guarani': 9, 'Router 3': 50},
    'Red Hat': {'Router 2': 25},
    'Guarani': {'Router 2': 9},
    'Router 3': {'Router 1': 43, 'Router 2': 50, 'Switch 2': 61},
    'Switch 2': {'Router 3': 61, 'Manjaro': 40, 'Parrot': 12, 'Fedora': 3, 'Arch': 56, 'MongoDB': 5},
    'Manjaro': {'Switch 2': 40},
    'Parrot': {'Switch 2': 12},
    'Fedora': {'Switch 2': 3},
    'Arch': {'Switch 2': 56},
    'MongoDB': {'Switch 2': 5}
}

# Aquí tuve que pedirle ayuda a la IA porque me arrojaba un error la carga
aristas_agregadas = set()
for origen, vecinos in grafo.items():
    for destino, peso in vecinos.items():
        clave = tuple(sorted([origen, destino]))
        if clave not in aristas_agregadas:
            g.add_edge(peso, origen, destino)
            aristas_agregadas.add(clave)

# B
notebooks = ["Red Hat", "Debian", "Arch"]
for nb in notebooks:
   print(f"Barrido en profundidad desde {nb}")
   g.deep_show(nb)
   print("---------------------------------------------------")

   print(f"Barrido en amplitud desde {nb}")
   g.amplitude_show(nb)
   print("---------------------------------------------------")

# C
def obtener_camino_mas_corto(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        return None, None
    
    paths_stack = grafo.dijkstra(origen)
    
    peso_total = None
    camino_completo = []
    nodo_actual = destino
    
    while paths_stack.size() > 0:
        value = paths_stack.pop()
        if value[0] == nodo_actual:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            nodo_actual = value[2]
            if nodo_actual is None:
                break
                
    camino_completo.reverse()
    return camino_completo, peso_total

pcs = ['Manjaro', 'Red Hat', 'Fedora']
for pc in pcs:
    camino, peso = obtener_camino_mas_corto(g, pc, 'Impresora')
    if camino:
        print(f"Desde {pc} a Impresora: {' -> '.join(camino)} (Costo: {peso})")
    else:
        print(f"No hay camino desde {pc} a Impresora")

print("-" * 60)

# D
print("Arbol de expansión mínima del grafo: ")
min_tree = g.kruskal("Arch")

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total}')
print("-" * 60)

# E
print("e. Camino más corto desde PCs al servidor 'Guarani':")
pcs_todas = ['Manjaro', 'Ubuntu', 'Mint', 'Fedora']
for pc in pcs_todas:
    camino, peso = obtener_camino_mas_corto(g, pc, 'Guarani')
    if camino:
        print(f"Desde {pc} a Guarani: {' -> '.join(camino)} (Costo: {peso})")
    else:
        print(f"No hay camino desde {pc} a Guarani")

print("Por lo tanto, el camino más corto es desde 'Ubuntu'.")
print("-" * 60)

# F
pos_switch1 = g.search('Switch 1', 'value')
computadoras_switch1 = []
for edge in g[pos_switch1].edges:
    pos_dest = g.search(edge.destination, 'value')
    tipo = g[pos_dest].other_values.get('tipo')
    if tipo in ['pc', 'notebook']:
        computadoras_switch1.append(edge.destination)

for comp in computadoras_switch1:
    camino, peso = obtener_camino_mas_corto(g, comp, 'MongoDB')
    if camino:
        print(f"Desde {comp} a MongoDB: {' -> '.join(camino)} (Costo: {peso})")
    else:
        print(f"No hay camino desde {comp} a MongoDB")
print("-" * 60)

# G
g.delete_edge("Switch 1", "Impresora")
g.add_edge(10, "Router 2", "Impresora")

notebooks = ["Red Hat", "Debian", "Arch"]
for nb in notebooks:
   print(f"Barrido en profundidad desde {nb}")
   g.deep_show(nb)
   print("---------------------------------------------------")

   print(f"Barrido en amplitud desde {nb}")
   g.amplitude_show(nb)
   print("---------------------------------------------------")