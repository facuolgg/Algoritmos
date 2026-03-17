#print("hola mundo", "desde python") # muestra algo en pantalla

#name = input('Ingrese su nombre: ', ) #input es read

#print('su nombre es: ', name)

# TIPOS DE DATOS PRIMITIVOS: STR, INT, FLOAT, BOOL, NONE

#variable = 'Ana'
#print(type[variable])
#variable = 1234
#print(type[variable])
#variable = 12.5
#print(type[variable])
#variable = True
#print(type[variable])

#number = int(input('ingrese un numero: '))
#print(number + 100)

# Funciones de conversion: int, str, float, bool(input'...')
# Estas convierten un tipo de dato a otro

# Funciones aritmeticas +,-,*,/, //, %, **
#print (5 + 2)
#print (5 - 2)
#print (5 * 2)
#print (5 / 2)
#print (5 // 2)
#rint (5 % 2)
#print (5 ** 2)

# Asignacion = --> a=10

# secuencial
# condicional
#    if - else | case
# ciclo
#    for | while
# operadores de control: >, <, >=, <=, ==, !=


num = 1 #int(input('Ingrese un numero: '))
if num > 5:
    print('es mayor')
elif num < 5:
    print('es menor')
else:
    print('es 5')

# elif es la suma de if+else, es mas simple

control = True
if control:
    print('se cumple el control')
# Si queremos comprobas si no se cumple el control, se usa if not
if not control:
    print('no se cumple el control')
# Operadores logicos: and, or, not, ^
if num >= 5 and num <= 10:
    print ('el numero esta entre 5 y 10')

# El case se usa de la siguiente manera
match num:

    case 1: print('es 1')
    case 5: print('es 5')
    
    case _: print('otro')

# Ciclo
#   for | while
# num = 1
# while num < 5:
#     print(num)
#     num += 1 #num = num + 1 

nums = [1, 2, 3, 4, 5]
nums.append(100)
# for i in range(len(nums)-1, 0, -1): # Muestra la lista de menor a mayor
#     print(nums)
# for i in range(len(nums)): # Si no le pongo valor inicial, lo toma como 0
#     print(nums[i])
# for number in nums:
#     print(number)


# Estructuras de datos: list, dic, tuple

# num_list = [None] * 10

# num_list = [1, 2, 3, 4]

# print(type(num_list))
# print(len(num_list))

# num_list.append(1)
# num_list.append(1)
# num_list.append(7)
# num_list.append(3) # Añade el número que le asignemos al final de la lista


# print(num_list)
# print(num_list.count(1)) # Cuenta la cantidad de elementos que hay de lo que le pidamos
# # print(num_list.index(2))
# # num_list.insert(21, 9)

# #num_list.pop() # Borra un numero de la posición que le asignemos (si no le asignamos, elimina el último)
# # print(num_list.remove()) # elimina el número que le pedimos por orden en que lo encuentra (si no le asignamos, elimina el primero)
# num_list.reverse #invierte la lista
# num_list.sort() # Ordena la lista (tiene que ser todo del mismo tipo) | (Reverse = True) para ordenar de mayor a menor
# print(num_list)
# print(num_list[4]) # Lo que está entre corchetes es la posición del elemento que desesamos mostrar

# Funciones y módulo

# def mi_funcion(num1, num2):
#     print('hola mundo')

#     num1 = num1 * 2
#     return num1 + num2, num1 - num2 # Devuelve una tupla (x, x, ...)

# n1 = 5
# n2 = 3
# suma, diferencia = mi_funcion(n1, n2)
# print(suma, diferencia)

# import sirve para importar módulos de otros programas
# import math

from math import sqrt as raiz_cuadrada

from mi_modulo import suma, diferencia

print(raiz_cuadrada(16))
# print(factorial(5))
print(suma(5, 3))
print(diferencia(5, 3))

dic = {32: "Juan", 45: "Hernán", 12: "Ana"} # Diccionario es una estructura de datos que almacena pares de clave-valor / clave -> valor
print (type(dic))

print(dic.get(124)) # Da la información según la clave que le pases

print(dic.keys()) # Muestra las claves del diccionario 

print(dic.values()) # Muestra los valores del diccionario

print(dic.items()) # Muestra las claves y los valores del diccionario

dic.pop(32) # Elimina la clave que le demos