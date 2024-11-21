"""
#6º

def palabra_escondida(frase, letra):
    contador_letra= 0
    contador_frase= 0

    for i in letra:
        contador_letra+=1
    for letra in frase:
        if letra == frase[contador_letra]:
            contador_letra+=1
        if letra
"""    

contenedora = "supercalifragilisticoespialidoso"
ejemplo = "rapido"

#6º (CORREGIDO)
def esta_palabra_escondida(palabra, cadena):
    
    esta_escondida = False

    if len(palabra) <= len(cadena):
        
        posicion_cadena=0
        posicion_palabra=0

        while posicion_cadena< len(cadena) and posicion_palabra <len(palabra):
            if cadena[posicion_cadena]==palabra[posicion_palabra]:
                posicion_palabra+=1

            posicion_cadena+=1
    if len(palabra)==posicion_palabra:
        esta_escondida=True

    return esta_escondida

assert(esta_palabra_escondida("rapido", "supercalifragilisticoespialidoso"))
assert(not esta_palabra_escondida("rapidxxx", "supercalifragilisticoespialidoso"))
assert(not esta_palabra_escondida("rapidos", "super"))