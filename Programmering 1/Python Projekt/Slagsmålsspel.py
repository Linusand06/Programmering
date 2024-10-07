import random
import time

while True:  

    namna = input("Choose Player A name: ")
    namnb = input("Choose Player B name: ")

    playera = 100
    playerb = 100

    while playera > 0 and playerb > 0:
        damage = random.randint(5, 15)
        playerb -= damage
        print("Player A hits player B with the force of", damage, "damage points")
        if playerb <= 0:
            print(namna, "has won!")
            break

        damage = random.randint(5, 15)
        playera -= damage
        print("Player B hits player A with the force of", damage, "damage points")
        if playera <= 0:
            print(namnb, "has won!")
            break

        print(namna, "has", playera, "HP left")
        print(namnb, "has", playerb, "HP left")


        time.sleep(1)

    restart = input("Do you want to play again? (yes/no): ").lower()
    if restart != "yes":
        print("Thanks for playing!")
        break
