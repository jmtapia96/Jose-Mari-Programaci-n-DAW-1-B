cadena_1= ["hola", "naranja", "tarde", "mandarina"]
cadena_2= ["adios", "hola", "mañana", "tarde"]


def intersect (cadena_1, cadena_2):
    lista_comun= []
    for palabra in cadena_1:
        if palabra in cadena_2 and palabra not in lista_comun:
            lista_comun.append(palabra)

    return (lista_comun)

print (intersect(cadena_1, cadena_2))

assert (intersect(["ipon", "Niddan", "Sandal"], ["Niddan", "Chodan", "Sandal"] == ["Niddan", "Sandal"]))

