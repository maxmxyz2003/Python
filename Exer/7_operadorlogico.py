#and devuelve true si v1=true y v2=true
#or devuelve true si v1=true o v2=true
#not devuelve true si v1=false o v2=false

from cgitb import reset

a=True
b=True
result= a and b
print(result)#true

b=False
result= a or b
print(result)#true

result= not b
print(result)#false