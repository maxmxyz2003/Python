numeros = int(input())
espacios = numeros // 2
n=1
for i in range(espacios,-1,-1):
    print(" "*i +"@"*(n))
    n+=2
    
