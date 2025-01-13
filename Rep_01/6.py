while True:
    tal=input("Ange ett heltal: ")

    try:
        nummer =int(tal)
        print("Du angav ett giltigt heltal")
        break
    except ValueError:
    
        print("Ogiltigt input")