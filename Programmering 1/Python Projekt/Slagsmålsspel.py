import random

namna=input("Skriv namn på spelare A: ")
namnb=input("Skriv namn på spelare B: ")

playera = 100
playerb = 100

while (playera >0 and playerb >0 ):
    damage = random.randint(5,15)
    playera -= damage
    print (damage)
    print("Player A hits player B with the force of ", damage, "damage points")
    if playera <= 0:
        print( "Player B has won!")
        break

    damage = random.randint(5,15)
    playerb -= damage
    print (damage)
    print("Player B hits player A with the force of ", damage, "damage points")
    if playerb <= 0:
        print("Player A has won!")
        break


else: 
    print("Tied!" )