from graph import Graph

g = Graph(is_dir=False)

ambientes = [
    'Cocina', 'Comedor', 'Cochera', 'Quincho', 
    'Baño 1', 'Baño 2', 'Habitación 1', 'Habitación 2', 
    'Sala de estar', 'Terraza', 'Patio'
]

for amb in ambientes:
    g.add_vertex(amb)

conexiones = [
    ('Cocina', 'Comedor', 5),
    ('Cocina', 'Baño 1', 5),
    ('Cocina', 'Patio', 7),
    ('Cocina', 'Quincho', 12),
    
    ('Comedor', 'Sala de estar', 8),
    ('Comedor', 'Habitación 1', 10),
    
    ('Cochera', 'Patio', 5),
    ('Cochera', 'Quincho', 5),
    ('Cochera', 'Baño 2', 6),
    
    ('Quincho', 'Patio', 4),
    
    ('Baño 1', 'Habitación 1', 4),
    ('Baño 1', 'Baño 2', 3),
    
    ('Baño 2', 'Habitación 2', 5),
    
    ('Habitación 1', 'Habitación 2', 5),
    
    ('Habitación 2', 'Sala de estar', 7),
    
    ('Sala de estar', 'Terraza', 5),
    ('Terraza', 'Patio', 6),
    ('Terraza', 'Quincho', 10),
]

for origen, destino, peso in conexiones:
    g.add_edge(peso, origen, destino)



# C
print("Arbol de expansión mínima del grafo: ")
min_tree = g.kruskal("Cocina")

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'metros totales: {peso_total}')
print(f"Por lo tanto, se necesitan {peso_total} metros de cable para conectar todos los ambientes.")
print("-" * 60)

# D
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

camino, peso = obtener_camino_mas_corto(g, "Habitación 1", 'Sala de estar')
if camino:
    print(f"Desde Habitación 1 a Sala de estar: {' -> '.join(camino)} (Costo: {peso})")
else:
    print(f"No hay camino desde Habitación 1 a Sala de estar")

print(f"Por lo tanto, se necesitan {peso} metros de cable de red para conectar el router con la Smart TV")