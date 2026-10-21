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
cola = Queue()
atendidos = []
N = int(input())
for _ in range(N):
    evento = input().split()
    if evento[0] == "FORMA":
        invitado = int(evento[1])
        if invitado not in atendidos and invitado not in cola.items:
            cola.enqueue(invitado)    
    elif evento[0] == "ATIENDE":
        if not cola.isEmpty():
            invitado = cola.dequeue()
            if invitado not in atendidos:
                print(f"SI TAMAL {invitado}")
                atendidos.append(invitado)
            else:
                print(f"NO TAMAL {invitado}")