"""
1º
"""
num_1= int(input("Introduzca el primer número. "))
num_2= int(input("Introduzca el segundo número. "))

if num_1<num_2:
    for i in range (num_1,num_2+1):
        print(i)
else:
    for i in range (num_2,num_1+1):
        print(i)

"""
2º
"""
numero= int(input ("introduzca un numero. "))
multiplicador=1

while multiplicador <=numero*10:
    print (multiplicador)
    multiplicador+=numero

"""
3º
"""
"""
Con for
"""
num_1= int(input("Introduzca el primer número. "))
num_2= int(input("Introduzca el segundo número. "))

if num_1<num_2:
    for i in range (num_1,num_2+1,7):
        print(i)
else:
    for i in range (num_2,num_1+1,7):
        print(i)
"""
Con while
"""
num_1= int(input("Introduzca el primer número. "))
num_2= int(input("Introduzca el segundo número. "))
num_final=1

while num_1<=num_2:
    if num_1%7==0:
        print (num_1)
    num_1+=1

"""
4º
"""
