hundar = ["spot", "scooby", "clifford", "Joel"]

print("mina hundar")
for i in range(0,len(hundar)):
    print (f"{i+1}) {hundar[i]}")

ans= int(input("vilken hund vill du använda"))

print(f"you chose {hundar[ans-1  ]}")
