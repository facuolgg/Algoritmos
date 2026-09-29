from queue_ import Queue
from heap import Heap

cola_prioridad = Heap()

# A 
print("Punto A:")
cola_prioridad.priority_arrive("Pedro.txt", 1)
cola_prioridad.priority_arrive("Walter.txt", 1)
cola_prioridad.priority_arrive("Ernesto.txt", 1)
print("Se cargaron los tres documentos de empleados exitosamente.")


# B
print("-" * 50)
print("Punto B: ")
print("El primer elemento de la cola es: ")
priority, value = cola_prioridad.elements[0]
print(value)

# C
print("-" * 50)
print("Punto C: ")
cola_prioridad.priority_arrive("Fernando.txt", 2)
cola_prioridad.priority_arrive("Dionisio .txt", 2)
# while cola_prioridad.size() > 0:
#     priority, value = cola_prioridad.priority_attention()
#     print(value)
print("Se cargaron dos documentos del staff de TI exitosamente.")

# D
print("-" * 50)
print("Punto D: ")
cola_prioridad.priority_arrive("Lara.txt", 3)
print("Cargado documento del gerente exitosamente.")

# E
print("-" * 50)
print("Punto E: ")
for i in (0, 1):
    print(f"Documento número {i+1} de la cola: ")
    priority, value = cola_prioridad.elements[i]
    print(value)

# F
print("-" * 50)
print("Punto F: ")
cola_prioridad.priority_arrive("Lucas.txt", 2)
cola_prioridad.priority_arrive("Facundo.txt", 2)
cola_prioridad.priority_arrive("Eric.txt", 3)
print("Cargados dos documentos de empleado y uno de gerente exitosamente.")

# G
print("-" * 50)
print("Punto G: ")
while cola_prioridad.size() > 0:
    priority, value = cola_prioridad.priority_attention()
    print(value)