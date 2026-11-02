from graph import Graph

g = Graph(is_dir=False)

# A
personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett',
    'C3PO', 'Leia', 'Rey', 'Kylo Ren',
    'Chewbacca', 'Han Solo', 'R2D2', 'BB8',
]

for p in personajes:
    g.add_vertex(p)

aristas = [
    ('Luke Skywalker', 'Darth Vader',  4),   
    ('Luke Skywalker', 'Yoda',         3),   
    ('Luke Skywalker', 'Leia',         4),   
    ('Luke Skywalker', 'Han Solo',     3),  
    ('Luke Skywalker', 'Chewbacca',    3),   
    ('Luke Skywalker', 'R2D2',        4),   
    ('Luke Skywalker', 'C3PO',        4),  
    ('Luke Skywalker', 'Boba Fett',    1),   
    ('Luke Skywalker', 'Rey',          1),  
    ('Luke Skywalker', 'Kylo Ren',     1), 

    ('Darth Vader',    'Yoda',         1),  
    ('Darth Vader',    'Leia',         2),   
    ('Darth Vader',    'Han Solo',     2),  
    ('Darth Vader',    'Chewbacca',    2),   
    ('Darth Vader',    'R2D2',        3),  
    ('Darth Vader',    'C3PO',        3),  
    ('Darth Vader',    'Boba Fett',    1),  
    ('Darth Vader',    'Kylo Ren',     1),   

    ('Yoda',           'Leia',         1),  
    ('Yoda',           'Chewbacca',    1),   
    ('Yoda',           'R2D2',        2),  
    ('Yoda',           'C3PO',        1),  
    ('Yoda',           'Boba Fett',    1),  
    ('Yoda',           'Rey',          1),   

    ('Boba Fett',      'Han Solo',     1),  
    ('Boba Fett',      'Chewbacca',    1), 
    ('Boba Fett',      'Leia',         1),  

    ('C3PO',          'Leia',         5),   
    ('C3PO',          'R2D2',        9),  
    ('C3PO',          'Han Solo',     3),   
    ('C3PO',          'Chewbacca',    3),   
    ('C3PO',          'Rey',          2),   
    ('C3PO',          'BB8',         2),   

    ('Leia',           'Han Solo',     4),   
    ('Leia',           'Chewbacca',    4),   
    ('Leia',           'R2D2',        5),   
    ('Leia',           'Rey',          2),  
    ('Leia',           'Kylo Ren',     2),  
    ('Leia',           'BB8',         1),  

    ('Rey',            'Kylo Ren',     3),  
    ('Rey',            'Chewbacca',    2),   
    ('Rey',            'Han Solo',     1),  
    ('Rey',            'R2D2',        1),   
    ('Rey',            'BB8',         3),  

    ('Kylo Ren',       'Han Solo',     1),   
    ('Kylo Ren',       'BB8',         1),   
    ('Kylo Ren',       'Chewbacca',    1),  
    ('Chewbacca',      'Han Solo',     4),   
    ('Chewbacca',      'R2D2',        3),   
    ('Chewbacca',      'BB8',         1),  

    ('Han Solo',       'R2D2',        3),   
    ('R2D2',          'BB8',         1),   
]

for origin, destination, weight in aristas:
    g.add_edge(weight, origin, destination)

# B
# En los grafos no dirigidos, los arboles mínimos de expansión son únicos, por lo que si busco el min_tree desde C3PO, Yoda o Leia, el resultado
# será el mismo. Por lo que solamente se hace la búsqueda desde C3PO.
print("Arbol de expansión mínima desde C3PO (que es igual desde cualquier otro vertice):")
min_tree = g.kruskal("C3PO")
print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total}')
print("-" * 60)

# C
# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden
#con dicho número
def max_episodios_compartidos():
    max_peso = -1
    pares = []

    for vertex in g:
        for edge in vertex.edges:
            if edge.weight > max_peso:
                max_peso = edge.weight
                pares = [(vertex.value, edge.destination)]
            elif edge.weight == max_peso:
                par = (vertex.value, edge.destination)
                par_inv = (edge.destination, vertex.value)
                if par not in pares and par_inv not in pares:
                    pares.append(par)

    print(f"Máximo de episodios compartidos: {max_peso}")
    print("Pares de personajes que coinciden:")
    for a, b in pares:
        print(f"   - {a} y {b}")
    return max_peso, pares


max_episodios_compartidos()
print("-" * 60)

# E
print("Camino más corto entre C3PO y R2D2: ")
exist_path = g.exist_path('C3PO', 'R2D2')

if exist_path:
    paths = g.dijkstra("C3PO")

    destination = 'R2D2'

    peso_total = None

    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()
    print(f'El camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

print("-" * 60)

print("Camino más corto entre Yoda y Darth Vader: ")
exist_path = g.exist_path('Yoda', 'Darth Vader')

if exist_path:
    paths = g.dijkstra("Yoda")

    destination = 'Darth Vader'

    peso_total = None

    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()
    print(f'El camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

print("-" * 60)

# F
def aparecen_en_los_9():
    encontrados = set()

    for vertex in g:
        for edge in vertex.edges:
            if edge.weight == 9:
                encontrados.add(vertex.value)
                encontrados.add(edge.destination)

    if not encontrados:
        print("No existen personajes que aparezcan en los 9 episodios.")
    else:
        print("Personajes que aparecen en los 9 episodios: ") 
        for p in sorted(encontrados):
            print(f" - {p}")

aparecen_en_los_9()
print("-" * 60)