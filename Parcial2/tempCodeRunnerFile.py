min_tree = g.kruskal('T')

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total}')