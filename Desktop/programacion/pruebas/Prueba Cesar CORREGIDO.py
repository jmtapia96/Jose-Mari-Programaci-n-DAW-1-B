CLAVE= "abcdefghjklmnñopqrstuvwxyz" #se deja mayuscula porque la variable no va a cambiar
LONGITUD= len(CLAVE)
def obtener_posicion_en_abecedario(caracter): #el index hace lo mismo
    posicion=0
    for i in range(LONGITUD):
        if caracter.lower() == CLAVE[i]: #Aqui miramos que el caracter recorra la cadena y ver si coincide
            posicion = i
    
    return posicion
def cifrar_caracter(caracter, desplazamiento):
    cifrado =""
    posición =0

    for i in range(LONGITUD):
        if caracter.lower() == CLAVE[i]: #Aqui miramos que el caracter recorra la cadena y ver si coincide
            posicion = i
    """
    if desplazamiento+posicion > LONGITUD
        cifrado= CLAVE[posicion+desplazamiento - LONGITUD]
    else:
        cifrado= CLAVE[posicion+desplazamiento]
    """

    obtener_posicion_en_abecedario (caracter)
    cifrado= CLAVE[(posicion+desplazamiento)%LONGITUD] # Haciendo el modulo permite que el desplazamiento que hagamos sea mayor a la cadena, ya que el resto, siempre dará la posición de la letra 

    return cifrado

def cifrar_palabra(palabra, desplazamiento):
    cifrada =""
    for letra in palabra: #sirve para otorgarle la posición a los caracteres
        cifrada+= cifrar_caracter(letra, desplazamiento) #el += sirve para que se vayan guardando las letras en la variable palabra ya cifrada

    return cifrada

assert(cifrar_palabra("casado",3)=="fdvdgr")
assert(cifrar_palabra("casado",1)== "dbtbep")
assert(cifrar_palabra("casado",0)== "casado")
assert(cifrar_palabra("casado",27)== "casado")

def son_equivalentes (palabra, cifrada):
    codificacion=-1
    desp=0
    while desp<LONGITUD and codificacion==-1:
        if cifrada == cifrar_palabra(palabra, desp): #con el while se evita que cuando se encuentre la codificación continue con la ejecución y valide con toda la LONGITUD
            codificacion=desp
        desp+=1

    """
    for desp in range (LONGITUD):
        if cifrada == cifrar_palabra(palabra, desp):
            codificacion=desp
    """
    return codificacion

print(cifrar_caracter("z", 23))


  