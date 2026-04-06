
# FACTORIAL !
#factorial(5) = 5 * 4 * 3 * 2 * 1
# 5 !

#fac(5) = 5 * fac(4)
#fac(4) = 4 * fac(3)
#fac(3) = 3 * fac(2)
#fac(2) = 2 * fac(1)
#fac(1) = 1 * fac(0)
#fac(0) = 1
#fac(N) = N * fac(N-1) -> fac(0) = 1

def factorial_r (num: int)-> int:
    if num == 0:
        return 1
    else:
        return num * factorial_r(num - 1)
        

def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result = result * i

    return result

#print(factorial(5))
#rint(factorial_r(5))


# Fibonacci


def fibonacci(num):
    fib_1 = 0
    fib_2 = 1
    for i in range(2, num + 1):
        fib_aux = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_aux
    return fib_aux

#print(fibonacci(50))

def fibonacci_r(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_r(num-1) + fibonacci_r(num-2)

#print(fibonacci_r(50))
# print(fibonacci_r(50)) # Esto tarda mucho tiempo, no es eficiente.

#Ejercicios:
#2) suma de todos los numeros enteros comprendidos entre cero y un numero entero positivo dado
#formula: n + (n-1) + (n-2) + ...
# sum(n)= n + sum(n-1)                         -->  sum(0) = 0 o sum(1) = 1

def sum_r(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num + sum_r(num-1)
    
print(sum_r(5))

#3) calcular el producto de dos numeros enteros dados
# prod(n,m) = n + prod(n, m-1)          -> n, m = 0 -> 0

def prod(n : int, m : int) -> int:
    if m==0:
        return 0
    else:
        return n + prod(n, m-1)

print(prod(2,3))

#7) h(n) ? 1/n + 1/(n-1) + 1/(n-2) + ... + 1  n = 1 -> 1

def serie_h(num : float) -> float:
    if num == 1:
        return 1
    else:
        return 1/num + serie_h(num-1)
    
print(serie_h(4))

#4) pot(n,m) = n ** m               -> pot(0,m) = 0, pot(n, 0) = 1

def pot(n : int, m : int) -> int:
    if n == 0:
        return 0
    elif m == 0:
        return 1
    else:
        return n * pot(n, m-1)

print(pot(5,3))

#10) contar la cantidad de dígitos de un número entero
# 523 -> 52     5           if n<10 = 1
        # +1      +1

def cont(n: int) -> int:
    if n <=10:
        return 1
    else:
        return 1 + cont(n // 10)

print(cont(5))
print(cont(52))
print(cont(523))
print(cont(5234))

#11) invertir número entero sin convertirlo a cadena



#14) suma de los dígitos de un número
#321 = 3 + 2 + 1                        n < 10 return n


#6) invertir secuencia de caracteres
#invertir(hola) = a + invertir(hol) -> cadena = ''

def invertir(cadena: str) -> str:
    if cadena == '':
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1]) # se aplicó slicing, que toma porciones de la cadena

print(invertir('casa'))