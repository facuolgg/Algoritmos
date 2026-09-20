# Ejercicio 22)
# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

mochila = ['Leche azul', 'Comida', 'Blaster de emergencia', 'Cristal de kyber rojo', 'Mortadela', 'Sable de luz']

def usar_la_fuerza(mochila: list, indice=0):
    if indice >= len(mochila):
        print('La mochila está vacía, no se encontró el sable de luz')
        return (False, 0)
    
    if mochila[indice] == 'Sable de luz':
        print(f'Sable de luz encontrado después de sacar {indice + 1} objetos')
        return (True, 1)
    
    found, count = usar_la_fuerza(mochila, indice + 1) 
    return (found, count + 1) 
    
# Prueba
print(usar_la_fuerza(mochila))

