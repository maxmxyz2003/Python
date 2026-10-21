# class Stack:
#     def __init__(self):
#         self.items = []    
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("pop from empty stack")
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("peek from empty stack")   
#     def is_empty(self):
#         return len(self.items) == 0
#     def size(self):
#         return len(self.items)

# stack = Stack()    
# stack.push(1)
# stack.push(2)
# stack.push(3)    
# print("Tamaño de la pila:", stack.size())  # Output: Tamaño de la pila: 3
# print("Elemento en la cima:", stack.peek())  # Output: Elemento en la cima: 3
# print("Elemento removido:", stack.pop())  # Output: Elemento removido: 3
# print("Elemento removido:", stack.pop())  # Output: Elemento removido: 2
# print("¿La pila está vacía?", stack.is_empty())  # Output: ¿La pila está vacía? False
# print("Elemento removido:", stack.pop())  # Output: Elemento removido: 1
# print("¿La pila está vacía?", stack.is_empty())  # Output: ¿La pila está vacía? True
# try:
#     stack.pop()
# except IndexError as e:
#     print(e)  # Output: pop from empty stack
# try:
#     stack.peek()
# except IndexError as e:
#     print(e)  # Output: peek from empty stack

class EasyStack:
    def __init__(self):
        self.stack = []
    def push(self, n):
        self.stack.append(n)
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print("Empty!")
def process_instructions(instructions):
    stack = EasyStack()
    for instruction in instructions:
        parts = instruction.split()
        p = int(parts[0])
        if p == 1:
            n = int(parts[1])
            stack.push(n)
        elif p == 2:
            stack.pop()
        elif p == 3:
            stack.top()

T = int(input())
instructions = [input() for _ in range(T)]
process_instructions(instructions)
