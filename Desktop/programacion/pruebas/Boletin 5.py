"""
2º
"""
n=7
contador=1
contador_par=2
contador_impar=2

while contador<n:
    if contador==1:
        print("1")
    elif contador%2==0:
        while contador_par<=contador:
            print("01"*(contador_par-1))
            contador_par+=2
    else:
        while contador_impar<=contador:
            print("101"*(contador-2))
            contador_impar+=2
    contador+=1

n=3
contador=1
contador_suma=1
while contador<=n:
   while contador_suma<=n:
     print(f"{1*contador_suma}" *contador)
     contador_suma+=1
     contador+=1

"""
8º
"""

"""
5º
"""

"""
Con for
"""

n_1=int(input("Introduce el primer número. " ))
n_2=int(input("Introduce el segundo número. "))

for i in range (n_1, (n_1+11)):
    if i%n_2==0:
        print (i)

"""
Con While
"""

n_1=int(input("Introduce el primer número. " ))
n_2=int(input("Introduce el segundo número. "))
contador=1


while contador<=n_1+10:
    if contador%n_2==0:
        print (contador)
    contador+=1

"""
10º
"""

edad= int(input("Dime cuantos años ha cumplido Juan. "))
contador=3
dinero_acu=20
puzzles_Acu=1

while contador<=edad:

    if contador%2==0:
        dinero_acu= dinero_acu*2+15



    else:
        puzzles_Acu= puzzles_Acu + (puzzles_Acu+1)
    contador+=1

if edad>=4:
    dinero_acu= dinero_acu-20

print(f"Cuando Juan tiene {edad} años, ha acumulado {puzzles_Acu} puzzles y {dinero_acu}€.")