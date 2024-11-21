"""
1º
"""

n=5
contador=1
total=0

while contador<=n:
    print("9"*contador):
    total += int("9"*contador)
    contador+=1

print(total)

"""
con funciones
"""

def suma_terminos(numero):
    contador=1
    total=0

    while contador<= numero:
        total+= int ("9"*contador)
        contador+=1

    return total

assert(suma_terminos(0)==0)
assert(suma_terminos(3)==1107)
assert(suma_terminos(4)==11106)

"""
10º
"""
edad= int(input("Dime cuantos años ha cumplido Juan. "))
contador=3
dinero_act=20
dinero_acu=20
puzzles_act=1
puzzles_Acu=1

while contador<=edad:

    if contador%2==0:
        dinero_acu+=dinero_act
        dinero_act+=15

    else:
        puzzles_Acu+=puzzles_act
        puzzles_act*=2
    contador+=1

print(f"Cuando Juan tiene {edad} años, ha acumulado {puzzles_Acu} puzzles y {dinero_acu}€.")