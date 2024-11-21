"""
explicación palisondromo
"""
cadena="palabra"
invertida= ""

for letra in cadena:
    invertida= letra + invertida

print (cadena, invertida)


"""
cadena="palabra"

def invertir (cadena):
    invertida= ""
    for letra in cadena:
        invertida= letra + invertida
    return invertida

assert (invertir("Hola, que tal?")== "?lat éuq, aloH")

print (cadena, invertir)
"""

"""
otra forma
"""

"""
def invertir(cadena):
    invertida=""
    #for i in range (len(cadena), -1, -1):
    #    invertida+=cadena[i]
    #for letra in cadena:
    #    invertida=letra+invertida
    for letra in cadena:
        invertida = letra + invertida


    return invertida

asser (invertir("Hola, que tal?")=="?lat euq ,aloH")
"""

def es_palindromo(cadena):
    return cadena == invertir(cadena)


def es_capicua(numero):
    return es_palindromo(str(numero))

def es_palindormo_otra_opcion(cadena):

    for i in range (len(cadena)//2):
        if cadena[i]!= cadena [len(cadena)-i -1]:
            resultado = False

    return resultado