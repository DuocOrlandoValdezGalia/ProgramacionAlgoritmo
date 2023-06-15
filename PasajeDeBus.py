menu = True
asientoComprado = []

bus = [
    ['A0', 'A1', 'A2'],
    ['B0', 'B1', 'B2'],
    ['C0', 'C1', 'C2'],
    ['D0', 'D1', 'D2'],
    ['E0', 'E1', 'E2'],
    ['F0', 'F1', 'F2'],
    ['G0', 'G1', 'G2'],
    ['H0', 'H1', 'H2'],
]


def ImprimirAsientos():
    asientos = "------- Bus -------\n"

    for fila in bus:
        for asiento in fila:
            if asientoComprado in asiento:
                asientos += "[ -- ]"
            else:
                asientos += f"[ {asiento} ]"

        asientos += "\n"

    return asientos

print(ImprimirAsientos())

def MenuGeneral():
    print("---- Buses Espedy gonzales ----")
    print("1) Mostrar Bus", "2) Comprar Pasaje", "3) Cancelar Pasaje", "4) Pagar Pasaje", "5) Cancelar Compra", "6) Salir", sep="\n")
    try:
        opcion = int(input("Seleccione una de las opciones disponibles: "))
        return opcion
    except:
        print("No disponible")



def ComprarAsientos():
     
    opcion = input("Ingrese el asiento que desea comprar: ")
    asientoComprado.append(opcion)



while menu:
    opcionElegidaMenu = MenuGeneral()

    match opcionElegidaMenu:
        case 1: 
            print(ImprimirAsientos())
            input()
            print("\n")

        case 2:
            print(ImprimirAsientos())
            ComprarAsientos()

        case _:
            print("Opcion no valida!\n")
