import random

tal=random.randint(1, 10)

guess=None

while guess != tal:
    gissning=input("Gissa talet: ")
    
    try:
        guess = int(gissning)

        if guess < tal:
            print("För lågt, försök igen!")

        elif guess > tal:
            print("För högt, försök igen!")
        
        else:
            print("Rätt svar!")
    except ValueError:
        print("Det var inte ett giltigt tal, försök igen!")