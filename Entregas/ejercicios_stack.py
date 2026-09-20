from stack import Stack
from random import randint
import copy


#pila = Stack()

# for i in range(10):
#     pila.push(randint(1, 10))

# Ejercicio 3
# print()
# pila.show()
# print()

# search_value = int(input('Ingrese un numero para remover sus ocurrencias: '))
# reemplazo = int(input('Ingrese un numero para reemplazar las ocurrencias: '))

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         pila_aux.push(reemplazo)
#     else:
#         pila_aux.push(value)

# while pila_aux.size() > 0:
#     value = pila_aux.pop()
#     pila.push(value)

# pila.show()

# Ejercicio 4
# print('Pila original:')
# pila.show()
# print()

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     pila_aux.push(value)

# print('Pila invertida:')
# pila_aux.show()

#Ejercicio 5
# pila = Stack()

# pila.push('O')
# pila.push('S')
# pila.push('O')


# pila_aux2 = Stack()
# pila_aux = Stack()


# while pila.size() > 0:
#     value = pila.pop()
#     pila_aux.push(value)
#     pila_aux2.push(value)


# while pila_aux2.size() > 0:
#     pila.push(pila_aux2.pop())

# print('Pila original:')
# pila.show()

# print('Pila invertida:')
# pila_aux.show()



# while pila.size() > 0 and pila_aux.size() > 0:
#     if pila.pop() != pila_aux.pop():
#         es_palindromo = False
#     else:
#         es_palindromo = True

# if es_palindromo:
#     print('La palabra es un palíndromo')
# else:
#     print('La palabra no es un palíndromo')

# Ejercicio 6
# pila = Stack()

# pila.push('S')
# pila.push('O')
# pila.push('M')
# pila.push('T')
# pila.push('I')
# pila.push('R')
# pila.push('O')
# pila.push('G')
# pila.push('L')
# pila.push('A')


# print('Pila con la palabra original:')
# pila.show()

# pila_aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     pila_aux.push(value)

# print('Pila con la palabra invertida:')
# pila_aux.show()

# Ejercicio 7
pila = Stack()
pila.push('Algoritmos')
pila.push('Arroz')
pila.push('Salame')
pila.push('Mate')
pila.push('Vino')


print('Pila original:')
pila.show()

print()
print('Cima: ', pila.cima_pila())
print()

print('Pila con el elemento debajo de la cima eliminado:')
if pila.size() >= 2:
        cima = pila.pop()
        pila.pop()
        pila.push(cima)
else:
    print('La pila no tiene suficientes elementos para eliminar el elemento debajo de la cima.')

pila.show()

