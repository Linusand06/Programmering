#Theo Green frågesport

#Fråga 1 Vilken snabbmatskedja är bäst, enligt Theo?

Rättsvar = 0
Rsvar1 = "B"

print ("Vilken snabbmatskedja är bäst enligt Theo?")
print ("A: Max")
print ("B: McDonalds")
print ("C: Burger King")

svar1 = input()

if(svar1 == Rsvar1):
    print("Rätt svar!")
    Rättsvar +=1
else: print("Fel svar!")

#Fråga 2 Vilket är bästa spelet som finns, enligt Theo?

Rsvar2 = "A"

print ("Vilket är bästa spelet någonsin, enligt Theo?")
print ("A: Roblox")
print ("B: Fortnite")
print ("C: Valorant")

svar2 = input()

if(svar2 == Rsvar2):
    print("Rätt svar!")
    Rättsvar +=1
else: print("Fel svar!")

#Fråga 3 Vad är Theos favoritmat? Pasta, Pommes eller Nudlar

Rsvar3 = "C"

print ("Vad är Theos favoritmat?")
print ("A: Nudlar")
print ("B: Pasta")
print ("C: Pommes")

svar3 = input()

if(svar3 == Rsvar3):
    print("Rätt svar!")
    Rättsvar +=1
else: print("Fel svar!")

print(f"Du fick {Rättsvar} rätt")
