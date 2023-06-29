import os
NombreCine = "Cinelocate"
ejecucion = True


asientosDelCine = [
    ['A1', 'A2', 'A3', 'A4'],
    ['B1', 'B2', 'B3', 'B4'],
    ['C1', 'C2', 'C3', 'C4'],
    ['D1', 'D2', 'D3', 'D4'],
    ['F1', 'F2', 'F3', 'F4'],
    ['G1', 'G2', 'G3', 'G4'],
]

asientosDelCineDisponibles = []
asientosComprados = []
personaReservada = []

def menu_General():
    os.system("cls")
    print(f"---------------- Bienvenidos a {NombreCine} ----------------\n")
    print("Entradas")
    print("1) Comprar entradas", "2) Ver asientos", "3) Impresion de compra", "4) Salir\n", sep="\n")
    try:
        opcionElegida = int(input("Ingrese alguna opción: "))
        return opcionElegida
    except:
        input("¡Ha ocurrido un error, presione enter para continuar!: ")

def MostrarAsientos():
    print("  |-------------------------------|")
    print("  |                               |")
    print("  |          BIENVENIDOS          |")
    print("  |              A SU             |")
    print("  |         CINE FAVORITO         |")
    print("  |                               |")
    print("  |-------------------------------|\n")
    dibujarCine = "\n"
    for i in asientosDelCine:
        for asientos in i:
            asientosDelCineDisponibles.append(asientos)

            if asientos in asientosComprados:
                dibujarCine += f" |( -- )|"    
            else:
                dibujarCine += f" |( {asientos} )|"
        
        dibujarCine += "\n"

    print(dibujarCine)

def comprarAsientoCine():
    asientoEscogido = input("Ingrese el asiento que desea: ")

    if asientoEscogido in asientosDelCineDisponibles:
        if not asientoEscogido in asientosComprados:
            asientosComprados.append(asientoEscogido)
            os.system("cls")
            ReservaDePersona(asientoEscogido)
            input(f"El Asiento {asientoEscogido}, fue registrado exitoxamente!")
        else:
            input("El asiento indicado se encuentra ocupado, por favor presione enter para continuar: ")
    else:
        input("El asiento indicado no existe, aprete enter para continuar: ")

def nombreVerificado():
    nombreVerificado = True

    while nombreVerificado:
        nombre = input("Nombre: ")

        if len(nombre) > 2 and len(nombre) <= 15:
            nombreVerificado = False
            return nombre
        else:
            input("El nombre debe tener 3 caracteres a 15 maximo, presione enter para continuar")

def apellidoVerificado():
    apellidoVerificado = True

    while apellidoVerificado:
        apellido = input("Apellido: ")

        if len(apellido) > 2 and len(apellido) <= 15:
            apellidoVerificado = False
            return apellido
        else:
            input("El nombre debe tener 3 caracteres a 15 maximo, presione enter para continuar")


def ReservaDePersona(asiento):
    print("Favor indique sus datos:")
    nombre = nombreVerificado()
    apellido = apellidoVerificado()

    personaReservada.append([asiento,nombre,apellido])

def impresionTicket():
    i = 1
    for personaQueReservo in personaReservada:
        print(f"--------------- TICKET {i} ---------------")
        print(f"Ticket: {personaQueReservo[0]}")
        print(f"Nombre: {personaQueReservo[1]}")
        print(f"Apellido: {personaQueReservo[2]}")
        print(f"------------------------------------------\n")
        i += 1

while ejecucion:
    opcionElegida = menu_General()

    match opcionElegida:
        case 1: 
            MostrarAsientos()
            comprarAsientoCine()
        case 2:
            MostrarAsientos()
            input("presione enter para continuar: ")
        case 3:
            if personaReservada == []:
                input("No se encuentran registros existentes, precione enter para continuar: ")
            else:
                impresionTicket()
                input("")
        case 4:
            input("Presione enter para salir del programa: ")
            ejecucion = False
        case _:
            input("¡Opcion elegida, no se encuentra dentro del rango! presione enter para continuar: ")