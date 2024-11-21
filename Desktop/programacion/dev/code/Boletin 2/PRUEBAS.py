player_1= 0
player_2= 0

while (player_1!= ("spock")) or (player_2!= ("spock")):
    player_1= input("Jugador 1, haga su elección. ")
    while player_1!= "tijera" and player_1!= "spock" and player_1!="lagarto" and player_1!="papel" and player_1!="piedra":
        player_1= input("Jugador 1, haga su elección. ")
        
    player_2= input("Jugador 2, haga su elección. ")
    while player_2!= "tijera" and player_2!= "spock" and player_2!="lagarto" and player_2!="papel" and player_2!="piedra":
        player_2= input("Jugador 2, haga su elección. ")

    if player_1== player_2:
        print("El jugador 1 ha empatado.")

    elif player_1== ("tijera"):
        if player_2== ("lagarto") or ("papel"):
            print("El jugador 1 ha ganado.")
        else:
            print("El jugador 1 ha perdido") 

    elif player_1== ("papel"):
        if player_2== ("spock") or ("piedra"):
            print("El jugador 1 ha ganado.")
        else:
            print("El jugador 1 ha perdido.")
   

    elif player_1== ("piedra"):
        if player_2== ("tijera") or ("lagarto"):
            print("El jugador 1 ha ganado.")
        else:
            print("El jugador 1 ha perdido.")
 

    elif player_1== ("lagarto"):
        if player_2== ("papel") or ("spock"):
            print("El jugador 1 ha ganado.")
        else:
            print("El jugador 1 ha perdido.")
  

    elif player_1== ("spock"):
        if player_2== ("tijera") or ("piedra"):
            print("El jugador 1 ha ganado.")
        else:
            print("El jugador 1 ha perdido.")
    

print("Los dos jugadores han empatado y han usado el elemento spock.")