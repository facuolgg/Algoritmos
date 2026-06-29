#apilar(pila, elemento) | agrega un elemento a la pila

#desapilar(pila) | elimina el elemento de la cima de la pila y lo devuelve

#pila_vacia(pila) |  devuelve True si la pila esta vacia, False en caso contrario

#cima_pila(pila) | devuelve el valor del elemento de la cima de la pila sin eliminarlo

#tamaño_pila(pila) | devuelve el número de elementos que hay en la pila

from typing import Any
import copy

class Stack:

    def __init__(self):
        self.__elements = [] #lista 

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:  #Le ponemos Any porque no sabemos que tipo de dato va a ser el que se desapile
        return self.__elements.pop()
    
    def pila_vacia(self) -> bool:
        if self.__elements == []:
            return print(True)
        else:
            return print(False)

    def show(self) -> None: #sacar
        stack_aux = Stack()
        stack_aux.__elements = copy.copy(self.__elements) #creamos una copia de la pila original para no perder los elementos de la pila original
        
        while stack_aux.size() > 0:
            value = stack_aux.pop()
            print(value)
        # stack_aux = Stack() #creamos una pila auxiliar para no perder los elementos de la pila original


        # while self.size() > 0:
        #     value = self.desapilar()
        #     print(value)
        #     stack_aux.apilar(value)

        # while stack_aux.size() > 0:
        #     value = stack_aux.desapilar()
        #     self.apilar(value)

    def size(self) -> int:
        return len(self.__elements)
    
    def cima_pila(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]

# pila = Stack()

# pila.push(1)
# #pila.show()

# pila.push(2)
# print(pila.cima_pila()) # Devuelve el valor del elemento de la cima de la pila sin eliminarlo

# #pila.__elements.clear() # Limpia la pila | Esto rompe el funcionamiento de la pila, pues solamente podemos insertar y eliminar de a 1

# pila.push(3)

# aux = pila.pop() # Elimina el elemento de la cima de la pila y lo devuelve
# print(f'Elemento desapilado: {aux}')


# pila.push(4)
# print(f'Cantidad de elementos en la pila: {pila.size()}') # Devuelve el número de elementos que hay en la pila

# pila.show()

#pila.pila_vacia()