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
contador_ing= 0
contador_ret= 0 
contador_total= 0

while eleccion!=4:
   if eleccion== 1:
       dinero_ingresar= int(input("¿Cuanto dinero desea ingresar? "))
       while dinero_ingresar<=0:
          print("La cantidad a ingresar no puede ser menor o igual que 0.")
           
       saldo+=dinero_ingresar
       contador_ing+=1
       contador_total+=1
       print(f"Operación {contador_total}: Ingreso realizado por valor de {dinero_ingresar}. Total: {saldo}")
       print(f"Se han efectuado {contador_ing} operaciones de ingresos y {contador_ret} de retirada.")

   elif eleccion== 2:
       dinero_retirar= int(input("¿Cuanto dinero desea retirar? "))
       while dinero_retirar<=0:
          print("La cantidad a retirar no puede ser menor o igual que 0.")
       while saldo<dinero_retirar:
          print("No dispone de sufciente dinero en su cuenta.")
       saldo-=dinero_retirar
       contador_ret+=1
       contador_total+=1
       print(f"Operación {contador_total}: Retirada realizada por valor de {dinero_retirar}. Total: {saldo}")
       print(f"Se han efectuado {contador_ing} operaciones de ingresos y {contador_ret} de retirada.")

   elif eleccion== 3:
    print(f"Dispone de un saldo de {saldo}€")

   print(MENU)
   eleccion= int(input("¿Que operación desea realizar? "))
print(f"Se han efectuado {contador_ing} operaciones de ingresos y {contador_ret} de retirada.")
print("Gracias por usar este cajero, Tapiacorp le desea un buen dia.")