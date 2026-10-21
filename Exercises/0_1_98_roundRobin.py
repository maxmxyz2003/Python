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

N, K = map(int, input().split())
procesos = Queue()
for _ in range(N):
    id_proceso, tiempo = map(int, input().split())
    procesos.enqueue((id_proceso, tiempo))
while not procesos.isEmpty():
    id_proceso, tiempo = procesos.dequeue()    
    if tiempo <= K:
        print(id_proceso)
    else:
        procesos.enqueue((id_proceso, tiempo - K))
