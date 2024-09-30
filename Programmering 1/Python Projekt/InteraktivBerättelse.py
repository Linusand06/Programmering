
print("Du befinner dig i en mystisk skog där stigen framför dig delar sig.")
print("Vad gör du?")
print("A) Följ den vänstra stigen.")
print("B) Följ den högra stigen.")

answer1 = input()

if answer1 == "A":
    print("Du följer den vänstra stigen och hör ett avlägset ljud. Vill du undersöka det?")
    print("A) Ja, undersök ljudet.")
    print("B) Nej, fortsätt på stigen.")

    answer2 = input()
    
    if answer2 == "A":
        print("Du går mot ljudet och upptäcker en gömd skatt i skogen!")
        print("Slut: Du hittade en skatt!")
    elif answer2 == "B":
        print("Du fortsätter att gå men plötsligt faller du ner i ett djupt hål.")
        print("Slut: Du fastnar i hålet.")
    else:
        print("Ogiltigt val.")

elif answer1 == "B":
    print("Du följer den högra stigen och stöter på en gammal stuga.")
    print("Vill du knacka på dörren?")
    print("A) Ja, knacka på dörren.")
    print("B) Nej, gå vidare.")

    answer2 = input()
    
    if answer2 == "A":
        print("En vänlig gammal kvinna öppnar dörren och bjuder dig på te.")
        print("Slut: Du får en trevlig kväll.")
    elif answer2 == "B":
        print("Du går vidare och hittar en vacker utsikt över hela skogen.")
        print("Slut: Du njuter av utsikten.")
    else:
        print("Ogiltigt val.")

else:
    print("Ogiltigt val.")
