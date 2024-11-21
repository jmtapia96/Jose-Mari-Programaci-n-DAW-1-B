"""
Bucles While
"""

numero= int(input ("introduzca un numero. "))
multiplicador=1

while multiplicador<=10:
    print(numero*multiplicador)
    multiplicador+=1

"""
multiplicando una sola vez
"""

numero= int(input ("introduzca un numero. "))
multiplicador=1

while multiplicador <=numero*10:
    print (multiplicador)
    multiplicador+=numero

"""
Bucles para los inputs (while)
"""

numero= int(input ("introduzca un numero. "))

while numero<0:
        numero= int(input ("Dato erroneo, por favo, introduzca un numero correcto. "))

if numero%2==0:
    print("es par")
else:
    print("es impar")

"""
Bucles para inputs con for

NO SE PUEDE

"""

