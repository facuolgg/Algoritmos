from stack import Stack

pila = Stack()
pila_inversa = Stack()

def movimiento (pila, direccion, pasos):
    direccion = direccion.lower()
    if direccion != "norte" and direccion != "sur" and direccion != "este" and direccion != "oeste" and direccion != "noroeste" and direccion != "noreste" and direccion != "suroeste" and direccion != "sureste":
        print("Direccion no valida")
    
    if pasos <= 0:
        print("Pasos no validos")

    #print(f"Movimiento: {direccion}, {pasos} pasos")

    pila.push((direccion, pasos))

def movimiento_inverso(pila):
    if pila == []:
        print("No hay movimientos para deshacer")
    else:
        while pila.size() > 0:
            direccion, pasos = pila.pop()
            if direccion == "norte":
                direccion_inversa = "sur"
            elif direccion == "sur":
                direccion_inversa = "norte"
            elif direccion == "este":
                direccion_inversa = "oeste"
            elif direccion == "oeste":
                direccion_inversa = "este"
            elif direccion == "noroeste":
                direccion_inversa = "sureste"
            elif direccion == "noreste":
                direccion_inversa = "suroeste"
            elif direccion == "suroeste":
                direccion_inversa = "noreste"
            elif direccion == "sureste":
                direccion_inversa = "noroeste"   
            
            pila_inversa.push((direccion_inversa, pasos))
    

# TEST
movimiento(pila, "norte", 3)
movimiento(pila, "este", 2)
movimiento(pila, "sur", 1)
movimiento(pila, "oeste", 4)
movimiento(pila, "sureste", 2)

pila.show()

print("------------------------")

movimiento_inverso(pila)

pila_inversa.show()
