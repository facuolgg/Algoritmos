from queue_ import Queue
from copy import deepcopy
from stack import Stack

# Ej 10
# hora, app, mensaje

class notificacion:

    def __init__ (self, hora, app, msj):
        self.hora = hora
        self.app = app
        self.msj = msj

    def __str__(self):
        return f"{self.hora} {self.app} {self.msj}"
    

queue = Queue()

queue.arrive(notificacion("12:00", "WhatsApp:", "Hola"))
queue.arrive(notificacion("4:00", "Facebook:", "Alejandro quiere ser tu amigo"))
queue.arrive(notificacion("12:01", "Telegram:", "Bienvenido a Telegram!"))
queue.arrive(notificacion("12:02", "Facebook:", "Alejandro le ha dado me gusta tu foto"))
queue.arrive(notificacion("15:16", "Twitter:", "Me encanta Python"))

queue.show()

def delete_facebook(queue):
    if queue.size() > 0:
         for i in range(queue.size()):
            notificacion_aux = queue.attention()
            if notificacion_aux.app == "Facebook:":
                print("Notificacion de Facebook eliminada")
                pass
            else:
                queue.arrive(notificacion_aux)
    else:
        print("No hay notificaciones en la cola")

def show_twitter_python(queue):
    if queue.size() > 0:
        for i in range(queue.size()):
            notificacion_aux = queue.attention()
            if notificacion_aux.app == "Twitter:" and "python" in notificacion_aux.msj.lower():
                print(notificacion_aux)
            queue.arrive(notificacion_aux)



print("-------------------------------")
delete_facebook(queue)

queue.show()

print("-------------------------------")
print("Notificaciones de Twitter que incluyen la palabra Python:")
show_twitter_python(queue)

#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
stack = Stack()


def count_notifications_between_hours(queue, stack):
    count = 0
    if queue.size() > 0:
        for i in range(queue.size()+1):
            notificacion_aux = queue.attention()
            if "11:43" <= notificacion_aux.hora <= "15:57":
                stack.push(notificacion_aux)
                count += 1
            queue.arrive(notificacion_aux)
    else:
        print("No hay notificaciones en la cola")
    return count

print(f"Cantidad de notificaciones entre 11:43 y 15:57: {count_notifications_between_hours(queue, stack)}")
