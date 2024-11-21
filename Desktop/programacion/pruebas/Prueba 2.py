
tamaño=int(input("Introduzca el número de trabajadores que dispone. "))
while tamaño<=0:
    tamaño=int(input("Introduzca el número de trabajadores que dispone. "))

contador=0
contador_py=0
contador_jav=0
contador_h=0
contador_m=0
media_edad=0

while contador<tamaño:
    lenguaje= input("Introduzca el lenguaje de programación que usa, siendo como opción válida Python o Java. ")
    while (lenguaje!="java") and (lenguaje!= "python"):
        lenguaje= input("Introduzca el lenguaje de programación que usa, siendo como opción válida Python o Java. ")
    if lenguaje=="java":
        contador_jav+=1
    elif lenguaje=="python":
        contador_py+=1
    edad= int(input("Introduzca su edad, la cual debe estar comprendida entre 18-65 años. "))
    while edad not in range(18,65+1):
        edad= int(input("Introduzca su edad, la cual debe estar comprendida entre 18-65 años. "))
    sexo= input("Introduzca su sexo, siendo como opción valida hombre o mujer. ")
    while sexo!="hombre" and sexo!= "mujer":
        sexo= input("Introduzca su sexo, siendo como opción valida hombre o mujer. ")
    if sexo=="hombre":
        contador_h+=1
    elif sexo=="mujer":
        contador_m+=1

    contador+=1
    media_edad= float(media_edad+edad)/contador

media_jav= float((contador_jav/tamaño)*100)
print (f"El {media_jav}% de empleados utiliza java, de los que {contador_h} son hombres y {contador_m} son mujeres. y su edad media es {media_edad} años.")    

media_py= float((contador_py/tamaño)*10)
print (f"El {media_py}% de empleados utiliza java, de los que {contador_h} son hombres y {contador_m} son mujeres. y su edad media es {media_edad} años.")