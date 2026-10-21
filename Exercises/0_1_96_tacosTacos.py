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

fila1=Queue()
tacos_vendidos = 0
N = int(input())
for _ in range(N):
    operacion = input().split()
    tipo_operacion = int(operacion[0])    
    if tipo_operacion == 1:
        tacos = int(operacion[1])
        fila1.enqueue(tacos)   
    elif tipo_operacion == 2:
        if not fila1.isEmpty():
            tacos_vendidos += fila1.dequeue()
    elif tipo_operacion == 3:
        print(fila1.size())    
    elif tipo_operacion == 4:
        print(tacos_vendidos)


