

edades= []

edades= [18, 23, 45]

#print(18 in edades)

edades[1]=25

#edades.remove(18) elimina todos los elementos que contengan esa variable de la lista
#edades.pop() #elimina el elemento que haya en la posición indicada


#calcular la media de las edades introducidas
for edad in edades:
    total+=edad
print(total/len(edades))

for edad in edades:
    print (edad)


numeros = []

for i in range (1,101):
    numeros.append(i)

print(numeros)

numeros.append("Se acabo") #se puede añadir cualquier tipo de dato con el append, indiferente si es str o int o float

print(numeros)

"""
Ejercicio de def fecha válida con listas
"""

año= int(input("Por favor introduzca el año. "))
mes= int(input("Por favor introduzca el mes. "))
dia= int(input("Por favor introduzca el día. "))

def es_año_bisiesto (año):
    return year%4==0 and year%100!=0 and year%400==0

def es_fecha_válida(dia, mes, año):
    lista_mes_31= [1,3,5,7,8,10,12]
    lista_mes_30= [4,6,9,11]
    lista_mes_28= [2]
    lista_dias_31= []
    for i in range (1,32):
        lista_dias_31.append(i)
    lista_dias_30= []
    for i in range (1,31):
        lista_dias_30.append(i)
    lista_dias_28= []
    for i in range (1,29):
        lista_dias_28.append(i)
    
    while año<=0:
        año= int(input("Por favor introduzca el año. "))
    while mes!= lista_mes_30 or lista_mes_31 or lista_mes_28:
        mes= int(input("Por favor introduzca el mes. "))
    while dia!= lista_dias_31 or lista_dias_30 or lista_dias_28:
        dia= int(input("Por favor introduzca el día. "))

    return True



es_fecha_válida (dia, mes, año)

"""
EJERCICIO CORREGIDO

def es_año_bisiesto (año):
    return year%4==0 and year%100!=0 and year%400==0

def es_fecha_valida (dia, mes, año):
    dias_maximos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 0<mes<13 and (0<dia<=dias_maximos [mes-1] or es_año_bisiesto(año) and mes==2 and 0<dia<=29)

BUSCAR CARACTERES EN UNA LISTA
    
nombres = ["Miguel", "Julio", "Ana", "Jose Manuel"]

print(nombres[0][0]) #en el primer [] seleccionas la posicición de la cadena y en el segundo la posición de la letra.

"""
"""
nombres = ["Miguel", "Julio", "Ana", "Jose Manuel"]

print(nombres[0][0]) #en el primer [] seleccionas la posicición de la cadena y en el segundo la posición de la letra.

"""