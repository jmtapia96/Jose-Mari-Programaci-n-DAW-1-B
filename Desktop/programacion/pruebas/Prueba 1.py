"""
1.1
"""
player_1= input("Jugador 1, haga su elección. ")
player_2= input("Jugador 2, haga su elección. ")

if player_1== player_2:
    print("El jugador 1 ha empatado.")

elif player_1== ("tijera"):
    if player_2== ("lagarto") or ("papel"):
        print("El jugador 1 ha ganado.")
    elif player_2== ("spock") or ("piedra"):
        print("El jugador 1 ha perdido") 

elif player_1== ("papel"):
    if player_2== ("spock") or ("piedra"):
        print("El jugador 1 ha ganado.")
    elif player_2== ("tijera") or ("lagarto"):
        print("El jugador 1 ha perdido.")
   

elif player_1== ("piedra"):
    if player_2== ("tijera") or ("lagarto"):
        print("El jugador 1 ha ganado.")
    elif player_2== ("papel") or ("spock"):
        print("El jugador 1 ha perdido.")
 

elif player_1== ("lagarto"):
    if player_2== ("papel") or ("spock"):
        print("El jugador 1 ha ganado.")
    elif player_2== ("tijera") or ("piedra"):
        print("El jugador 1 ha perdido.")
  

elif player_1== ("spock"):
    if player_2== ("tijera") or ("piedra"):
        print("El jugador 1 ha ganado.")
    elif player_2== ("papel") or ("spock"):
        print("El jugador 1 ha perdido.")
 
else:
        print("Por favor, introducid una opción válida.")

"""
1.2
"""

player_1= 0
player_2= 0

while (player_1!= ("spock")) or (player_2!= ("spock")):
    player_1= input("Jugador 1, haga su elección. ")
    player_2= input("Jugador 2, haga su elección. ")
    

    if player_1== player_2:
        print("El jugador 1 ha empatado.")

    elif player_1== ("tijera"):
        if player_2== ("lagarto") or ("papel"):
            print("El jugador 1 ha ganado.")
        elif player_2== ("spock") or ("piedra"):
            print("El jugador 1 ha perdido") 

    elif player_1== ("papel"):
        if player_2== ("spock") or ("piedra"):
            print("El jugador 1 ha ganado.")
        elif player_2== ("tijera") or ("lagarto"):
            print("El jugador 1 ha perdido.")
   

    elif player_1== ("piedra"):
        if player_2== ("tijera") or ("lagarto"):
            print("El jugador 1 ha ganado.")
        elif player_2== ("papel") or ("spock"):
            print("El jugador 1 ha perdido.")
 

    elif player_1== ("lagarto"):
        if player_2== ("papel") or ("spock"):
            print("El jugador 1 ha ganado.")
        elif player_2== ("tijera") or ("piedra"):
            print("El jugador 1 ha perdido.")
  

    elif player_1== ("spock"):
        if player_2== ("tijera") or ("piedra"):
            print("El jugador 1 ha ganado.")
        elif player_2== ("papel") or ("spock"):
            print("El jugador 1 ha perdido.")
 
    else:
            print("Por favor, introducid una opción válida.")
    

print("Los dos jugadores han empatado y han usado el elemento spock.")