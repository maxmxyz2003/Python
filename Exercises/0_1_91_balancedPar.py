class Stack:
    def __init__(self):
        self.items = []    
    def push(self, item):
        self.items.append(item)
    def pop(self):
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

def parBal(str):
    s=Stack()
    for i in str:
        if i==")" or i=="}" or i=="]" and s.is_empty():
            return "NO"
        if i=="[" or i=="(" or i=="{":
            s.push(i)
        elif i=="]":
            if s.peek()=="[":
                s.pop()
            else:
                return "NO"
        elif i==")":
            if s.peek()=="(":
                s.pop()
            else:
                return "NO"
        elif i=="}":
            if s.peek()=="{":
                s.pop()
            else:
                return "NO"
    return "YES"

n=int(input())
for i in range(n):
    string=input()
    print(parBal(string))

"""#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>


struct nodo {
    char simbolo;
    struct nodo *sig;
};

struct nodo *raiz=NULL;

void insertar(char x)
{
    struct nodo *nuevo;
    nuevo = malloc(sizeof(struct nodo));
    nuevo->simbolo = x;
    if (raiz == NULL)
    {
        raiz = nuevo;
        nuevo->sig = NULL;
    }
    else
    {
        nuevo->sig = raiz;
        raiz = nuevo;
    }
}


char extraer()
{
    if (raiz != NULL)
    {
        char informacion= raiz->simbolo;
        struct nodo *bor = raiz;
        raiz = raiz->sig;
        free(bor);
        return informacion;
    }
    else
    {
        return -1;
    }
}

void liberar()
{
    struct nodo *reco = raiz;
    struct nodo *bor;
    while (reco != NULL)
    {
        bor = reco;
        reco = reco->sig;
        free(bor);
    }
}

int vacia()
{
    if (raiz == NULL)
        return 1;
    else
        return 0;
}

void cargarFormula(char *formula)
{
    printf("Ingrese la formula:");
    gets(formula);
}

int verificarBalanceada(char *formula)
{
    int f;
    for (f=0;f<strlen(formula);f++)
    {
        if (formula[f]=='(' || formula[f]=='[' || formula[f]=='{')
        {
            insertar(formula[f]);
        }
        else
        {
            if (formula[f]==')')
            {
                if (extraer()!='(')
                {
                    return 0;
                }
            }
            else
            {
                if (formula[f]==']')
                {
                    if (extraer()!='[')
                    {
                        return 0;
                    }
                }
                else
                {
                    if (formula[f]=='}')
                    {
                        if (extraer()!='{')
                        {
                            return 0;
                        }
                    }
                }
            }
        }
    }
    if (vacia())
    {
        return 1;
    }
    else
    {
        return 0;
    }
}


int main()
{
    char formula[100];
    cargarFormula(formula);
    if (verificarBalanceada(formula))
    {
        printf("La formula esta correctamente balanceada");
    }
    else
    {
        printf("La formula no esta correctamente balanceada");
    }
    liberar();
    getch();
    return 0;
}
"""
