# Ejercicio 5)
# Desarrollar una función que permita convertir un número romano en un número decimal.
# Si n = '', entonces devuelve 0 
# Ejemplo: 'XII' -> 12, 'IV' -> 4

def valor_romano(caracter: str) -> int:
    if caracter == 'I':
        return 1
    elif caracter == 'V':
        return 5
    elif caracter == 'X':
        return 10
    elif caracter == 'L':
        return 50
    elif caracter == 'C':
        return 100
    elif caracter == 'D':
        return 500
    elif caracter == 'M':
        return 1000
    else:
        return 0
    
def romano_a_decimal(romano: str) -> int:
    if romano == '':
        return 0
    
    if len(romano) == 1:
        return valor_romano(romano[0])
    
    primero = valor_romano(romano[0])
    segundo = valor_romano(romano[1])

    if primero < segundo:
        return -primero + romano_a_decimal(romano[1:])
    else:
        return primero + romano_a_decimal(romano[1:])
    
# Pruebas
print(romano_a_decimal('XII'))
print(romano_a_decimal('IV'))
print(romano_a_decimal('MDC'))
print(romano_a_decimal(''))
