class DeuxMilleQuaranteHuit:
    def __init__(self):
        self.items = []    
    def push(self, item):
        self.items.append(item)
        print(self.items)
        if self.size()>1:
            self.simplify()
        print(self.items)        
    def Pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    def simplify(self):
        s=self.size()
        i=0
        while s>i:
            if self.items[i]==self.items[i+1]:
                self.items.pop(i)
                self.items[i]*=2
                s-=1
            s-=1
            i+=1
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")   
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

n=int(input())
s=DeuxMilleQuaranteHuit()
for i in range(n):
    x=int(input())
    s.push(x)

for i in range(n):
    s.simplify()

print(s.size())
print(s.items[::-1])    

