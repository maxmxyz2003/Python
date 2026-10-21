class StackQ:
    def __init__(self):
        self.items = []
        self.mode=1

    def switch(self):
        self.mode*=-1
    def add(self,i):
        if self.mode==1:
            self.push(i)
        else:
            self.enqueue(i)
    def delet(self):
        if not self.is_empty():
            if self.mode==1:
                return self.Pop()
            else:
                return self.dequeue()
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def enqueue(self,item):
        self.items.append(item)
    def Pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "pop from empty stack"
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Empty Queue"
    def Rear(self):
        if not self.is_empty():
            return self.items[self.size()-1]
    def Front(self):
        if not self.is_empty():
            return self.items[0]


pila_cola = []
pila_cola=StackQ()
N = int(input())
for _ in range(N):
    evento = input().split()    
    if evento[0] == "AGREGA":
        valor = int(evento[1])
        pila_cola.add(valor)    
    elif evento[0] == "QUITA":
        print(pila_cola.delet())
    elif evento[0] == "CAMBIA":
        pila_cola.switch()