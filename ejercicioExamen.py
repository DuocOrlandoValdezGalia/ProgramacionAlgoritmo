import os
i = True
asientos = "··········· Bus ···········\n"
asientosComprado = []
asientos_comprados = []
asientos_del_bus = []
pasajeroBus = []
bus = [
    ["A1","A2","A3","A4"],
    ["B1","B2","B3","B4"],
    ["C1","C2","C3","C4"],
    ["D1","D2","D3","D4"],
    ["E1","E2","E3","E4"],
    ["F1","F2","F3","F4"],
    ["G1","G2","G3","G4"],
    ["H1","H2","H3","H4"],
    ["I1","I2","I3","I4"],
    ["J1","J2","J3","J4"],
    ["K1","K2","K3","K4"],
    ["L1","L2","L3","L4"],
    ["M1","M2","M3","M4"],
    ["N1","N2","N3","N4"],
    ["O1","O2","O3","O4"],
]


def menuGeneral():
    os.system("cls")
    print("··························", "··· Gestion de viajes ···", "··························", sep="\n")
    print("1) Registrar viaje", "2) Mostrar asientos", "3) Mostrar informacion de viaje", "4) Mostrar informacion de todos los viajes", "5) Salir", sep="\n")
    try:
        opcionElegida = int(input("Ingrese una de las opciones: "))
        return opcionElegida
    except:
        input("Ha ocurrido un error!, presione enter para continuar: ")

def RegistroViaje():
    print("")

def MostrarViajeReservado():
    os.system("cls")
    i_asientos = "········· BUS ·········\n"

    for fila in bus:
        for asiento in fila:
            
            asientos_del_bus.append(asiento)

            if asiento in asientosComprado:
                i_asientos += "[ -- ]"
            else:
                i_asientos += f"[ {asiento} ]"
        
        i_asientos += "\n"

    print(i_asientos)

def comprar_asiento():
    opcion = input("Ingrese el asiento que desea utilizar: ")

    if opcion in asientos_del_bus:
        if not opcion in asientosComprado:
            asientosComprado.append(opcion)
            os.system("cls")
            persona_pasaje(opcion)
            input(f"El asiento {opcion}, fue registrado")
        else:
            input("El asiento indicado se encuentra ocupado, por favor presione enter para continuar: ")
    else:
        input("El asiento indicado no existe, aprete enter para continuar: ")

def TelefonoVerificado():
    telefonoVerificado = True
    
    while telefonoVerificado:
        try:
            telefono = input("Telefono Emergencia: ")

            if len(telefono) == 9:
                telefonoVerificado = False
                return telefono
            else:
                input("El telefono debe tener 9 digitos, presione enter para continuar: ")

        except:
            input("Ha ocurrido un error!, presione enter para continuar: ")

def verificacionRUT():
    verificacionRUT = True

    while verificacionRUT:
        try:
            rut = input("Rut: ")
            if len(rut) == 12:
                verificacionRUT = False
                return rut
            else:
                input("El rut debe tener 12 digitos, presione enter para continuar: ")
        except:
            input("Ha ocurrido un error!, presione enter para continuar: ")  

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

def direccionVerificado():
    direccionVerificado = True

    while direccionVerificado:
        direccion = input("direccion: ")

        if len(direccion) > 2 and len(direccion) <= 20:
            direccionVerificado = False
            return direccion
        else:
            input("La direccion debe tener 3 caracteres a 20 maximo, presione enter para continuar")

def origenVerificado():
    origenVerificado = True

    while origenVerificado:
        origen = input("Origen: ")

        if len(origen) > 2 and len(origen) <= 20:
            origenVerificado = False
            return origen
        else:
            input("El origen debe tener 3 caracteres a 20 maximo, presione enter para continuar")

def destinoVerificado():
    destinoVerificado = True

    while destinoVerificado:
        destino = input("Destino: ")

        if len(destino) > 2 and len(destino) <= 20:
            destinoVerificado = False
            return destino
        else:
            input("El destino debe tener 3 caracteres a 20 maximo, presione enter para continuar")

def persona_pasaje(asiento):
    print("Favor indique sus datos:")
    rut = verificacionRUT()
    nombre = nombreVerificado()
    apellido = apellidoVerificado()
    direccion = direccionVerificado()
    origen = origenVerificado()
    destino = destinoVerificado()
    telefonoEmergencia = TelefonoVerificado()

    pasajeroBus.append([asiento,rut,nombre,apellido, direccion, origen, destino, telefonoEmergencia])

while i:
    opcionElegida = menuGeneral()

    match opcionElegida:
        case 1:
            MostrarViajeReservado()
            comprar_asiento()
        case 2:
            MostrarViajeReservado()
            input("precione enter para continuar: ")
        case 5:
            input("presione enter para salir del programa: ")
            i = False
        case _:
            input("Opcion elegida no valida, presione enter para continuar: ")