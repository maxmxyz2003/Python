class Queue:
    def __init__(self):
        self.items=[]
        self.limit=100
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "Empty Queue"
    def Rear(self):
        if not self.isEmpty():
            return self.items[self.size()-1]
    def Front(self):
        if not self.isEmpty():
            return self.items[0]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size()==0

cola_alumnos = Queue()
cola_trabajadores = Queue()
N = int(input())
for _ in range(N):
    evento = input().split()
    tipo_evento = evento[0]    
    if tipo_evento == "LLEGA":
        tipo_persona = evento[1]
        nombre = evento[2]
        if tipo_persona == "ALUMNO":
            cola_alumnos.enqueue(nombre)
        elif tipo_persona == "TRABAJADOR":
            cola_trabajadores.enqueue(nombre)    
    elif tipo_evento == "ATIENDE":
        if not cola_trabajadores.isEmpty():
            print(f"-{cola_trabajadores.dequeue()}")
        else:
            print(f"-{cola_alumnos.dequeue()}")
