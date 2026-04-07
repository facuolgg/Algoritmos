#apilar(pila, elemento) | agrega un elemento a la pila

#desapilar(pila) | elimina el elemento de la cima de la pila y lo devuelve

#pila_vacia(pila) |  devuelve True si la pila esta vacia, False en caso contrario

#cima_pila(pila) | devuelve el valor del elemento de la cima de la pila sin eliminarlo

#tamaño_pila(pila) | devuelve el número de elementos que hay en la pila

from typing import Any

class Stack:

    def __init__(self):
        self.__elements = [] #lista 

    def apilar(self, value: Any) -> None:
        self.__elements.append(value)

    def desapilar(self) -> Any:
        return self.__elements.pop()
    
    def pila_vacia(self) -> bool:
        if self.__elements == []:
            return print(True)
        else:
            return print(False)

    def show(self) -> None:
        print(self.__elements)


pila = Stack()

pila.apilar(1)
pila.show()

pila.apilar(2)
pila.show()

#pila.__elements.clear() # Limpia la pila | Esto rompe el funcionamiento de la pila, pues solamente podemos insertar y eliminar de a 1

pila.apilar(3)
pila.show()

pila.desapilar()

pila.apilar(4)
pila.show()

pila.pila_vacia()