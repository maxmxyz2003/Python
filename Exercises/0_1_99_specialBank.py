class Stack:
    def __init__(self):
        self.items = []    
    def push(self, item):
        self.items.append(item)
    def Pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")   
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
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

fila_1 =Queue()
fila_2 = Stack()
N = int(input())
for _ in range(N):
    evento = input().split()
    tipo_evento = evento[0]    
    if tipo_evento == "E":
        fila = int(evento[1])
        nombre = evento[2]        
        if fila == 1:
            fila_1.enqueue(nombre)
        elif fila == 2:
            fila_2.push(nombre)     
    elif tipo_evento == "A":
        fila = int(evento[1])        
        if fila == 1:
            print(fila_1.dequeue().lower())
        elif fila == 2:
            print(fila_2.Pop().lower())
