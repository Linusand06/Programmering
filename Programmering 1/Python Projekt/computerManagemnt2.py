

datorer = ["skola", "arbete", "personlig", "Microsoft", "Windows"]

service = []

while True:
    print("Alla datorer i företaget:")
    for i in range(0,len(datorer)):
        print (f"{i+1}) {datorer[i]}")

    print("Datorer på service:")
    for i in range(0,len(service)):
        print (f"{i+1}) {service[i]}")

    service_dator = int(input("Vilken dator ska in på service? ")) -1

    dator = datorer[service_dator]
    datorer.remove(dator)
    service.append(dator)

    print("Alla datorer i företaget:")
    for i in range(0,len(datorer)):
        print (f"{i+1}) {datorer[i]}")

    print("Datorer på service:")
    for i in range(0,len(service)):
        print (f"{i+1}) {service[i]}")

    if len(service) >= 3:
        print("Klar!")
        break
        