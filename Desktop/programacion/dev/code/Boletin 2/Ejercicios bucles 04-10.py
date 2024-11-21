
"""
1º Hacer una cuenta atrás para el cohete, que cuente de 10 hasta 0
"""
for i in range(10,-1,-1):
    print (i)
print ("IGNICION")
""""


2º Plasmar números pares del 2 al 50
"""

print ("---"*10)
for i in range(0,51,2):
    print (i)
print("---"*10)
"""""


3º muestrame la tabla de multiplicar de un número, pero usando solo la multiplicación una vez y otra que no se pueda multplicar

UNA SOLUCIÓN
"""
num= int(input(("introduce la tabla de multiplicar que quieres ver " )))
print("---"*10)
for i in range(num,(num*10+1),num):
    print (i)
print("---"*10)
"""""
OTRA SOLUCION:
"""
num= int(input(("introduce la tabla de multiplicar que quieres ver " )))
print (num)
print (num+num)
print (num+num+num)
print (num+num+num+num)
print (num+num+num+num+num)
print (num+num+num+num+num+num)
print (num+num+num+num+num+num+num)
print (num+num+num+num+num+num+num+num)
print (num+num+num+num+num+num+num+num+num)
print (num+num+num+num+num+num+num+num+num+num)
print("---"*10)