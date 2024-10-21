

datorer = ["skola", "arbete", "personlig", "Microsoft", "Windows"]

service = []

while True:
    print(f"Alla datorer i företaget: {datorer}")
    print(f"Datorer i service: {service}")

    service_dator = input("Vilken dator ska in på service?")

    if service_dator in datorer:
            datorer.remove(service_dator)
            service.append(service_dator)

    print(f"Alla datorer i företaget: {datorer}")
    print(f"Datorer i service: , {service}")

    if len(service) >= 3:
        print("Klar!")
        break
        