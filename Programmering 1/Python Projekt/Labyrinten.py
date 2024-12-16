def room_a():
    print("\nDu är i Rum A. Det är ett ljust rum med en dörr åt två håll.")
    print("Du kan gå till:")
    print("1. Rum B")
    print("2. Rum D")
    choice = input("Välj ett rum (1 eller 2): ").strip()
    if choice == "1":
        room_b()
    elif choice == "2":
        room_d()
    else:
        print("Ogiltigt val. Försök igen.")
        room_a()

def room_b():
    print("\nDu är i Rum B. Det är ett mörkt rum med två utgångar.")
    print("Du kan gå till:")
    print("1. Rum A")
    print("2. Rum C")
    choice = input("Välj ett rum (1 eller 2): ").strip()
    if choice == "1":
        room_a()
    elif choice == "2":
        room_c()
    else:
        print("Ogiltigt val. Försök igen.")
        room_b()

def room_c():
    print("\nDu är i Rum C. Ett kusligt rum med en utgångsskylt.")
    print("Du kan gå till:")
    print("1. Rum B")
    print("2. Rum D")
    print("Skriv 'exit' för att avsluta spelet.")
    choice = input("Välj ett rum (1, 2 eller 'exit'): ").strip()
    if choice == "1":
        room_b()
    elif choice == "2":
        room_d()
    elif choice.lower() == "exit":
        print("Spelet avslutas. Tack för att du spelade!")
    else:
        print("Ogiltigt val. Försök igen.")
        room_c()

def room_d():
    print("\nDu är i Rum D. Det är ett hemligt rum med en märklig känsla.")
    print("Du kan gå till:")
    print("1. Rum A")
    print("2. Rum C")
    choice = input("Välj ett rum (1 eller 2): ").strip()
    if choice == "1":
        room_a()
    elif choice == "2":
        room_c()
    else:
        print("Ogiltigt val. Försök igen.")
        room_d()

def start_game():
    print("Välkommen till Labyrinten v1!")
    print("Utforska labyrinten och hitta vägen ut.")
    room_a()

# Starta spelet
start_game()
