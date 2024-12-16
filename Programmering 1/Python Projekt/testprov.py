def math():
    Rsvar = 7

    gissning = 0

    print ("Du har i uppgift att räkna ut vad X står för i ett matteproblem.")
    print ("X * 6 = 42")

    while True:
        try:
            gissning= int(input("Vad är X? "))
            break
        except ValueError:
            print("Fel: Ange ett giltigt nummer!")


    if gissning < Rsvar:
        print("För lågt! Rätt svar är 7 * 6 = 42")
    elif gissning > Rsvar:
        print("För Högt! Rätt svar är 7 * 6 = 42")
    else:
        print("Rätt svar! Du fick 1 poäng.")


math()