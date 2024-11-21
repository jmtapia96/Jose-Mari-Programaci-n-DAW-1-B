MENU="""
    Seleccione una opción:
    1. Ingresar efectivo
    2. Retirar efectivo
    3. Consultar saldo
    4. Salir.
"""

print(MENU)
eleccion= int(input("¿Que operación desea realizar? "))
saldo= 0

while eleccion!=4:
    if eleccion== 1:
        dinero_ingresar= int(input("¿Cuanto dinero desea ingresar? "))
        if dinero_ingresar<=0:
            print("Cantidad.")
        saldo+=dinero_ingresar
    elif eleccion== 2:
        dinero_retirar= int(input("¿Cuanto dinero desea retirar? "))
        if saldo<dinero_retirar:
            print("No dispone de sufciente dinero en su cuenta.")
        else:
            saldo-=dinero_retirar
    elif eleccion== 3:
        print(f"Dispone de un saldo de {saldo}€")
    
    print(MENU)
    eleccion= int(input("¿Que operación desea realizar? "))