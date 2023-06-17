from operator import index
import os

nombreAgencia = "Auto Seguro"
multasVehiculos = []
datosVehiculo = []
i = True

def menu_general():
    os.system("cls")
    print("############################", f"\t{nombreAgencia}", "############################", sep="\n")
    print("1) Grabar", "2) Buscar", "3) Imprimir certificado", "4) Salir", sep="\n")
    try:
        opcionElegida = int(input("Ingrese la opcion a elegir: "))
        return opcionElegida
    except:
        print("La opcion elegida, no es valida!")

def ValidarPatente():
    pantenteEnValidacion = True

    while pantenteEnValidacion:
        patente = input("Patente: ")

        if len(patente) == 6:
            pantenteEnValidacion = False
            return patente
        else:
            input("Error al guardar la patente, presione enter para continuar: ")

def ValidarMarca():
    validarMarca = True
    while validarMarca:
        marca = input("Marca: ")

        if len(marca) > 1 and len(marca) < 16:
            return marca
        else:
            input("Error al guardar la marca, precione enter para continuar: ")

def ValidarPrecio():
    validarPrecio = True

    while validarPrecio:
        precio = int(input("Precio: "))

        if precio > 5000000:
            return precio
        else:
            input("Error al guardar la precio, precione enter para continuar: ")

def ValidarMultas(indexPatente):
    validarMulta = True

    while validarMulta:
        print("Usted Posee multas?", "1) Si", "2) No", sep="\n")
        poseeMulta = int(input("ingrese una opcion: "))
            
        if poseeMulta == 1:
            CantidadMultas = int(input("Ingrese la cantidad de multas que posee: "))
            acumulador = 1

            while acumulador <= CantidadMultas:
                descripcionMulta = input(f"Ingrese el motivo de la multa {acumulador}: ")
                multasVehiculos.append([indexPatente, descripcionMulta, acumulador])
                acumulador += 1
            
            
            validarMulta = False
            return multasVehiculos

        else:
            validarMulta = False
            return 0



def GuardarDatosVehiculo():
    tipo = input("Tipo: ")
    patente = ValidarPatente()
    marca = ValidarMarca()
    precio = ValidarPrecio() 
    multas = ValidarMultas(patente)
    fechaRegistro = input("Fecha Registro: ") 
    nombreDueno = input("Nombre Dueno: ")

    datosVehiculo.append([tipo, patente, marca, precio, multas, fechaRegistro, nombreDueno])
    
    input("¡Se ha guadado exitosamente los datos!, presiona enter para continuar: ")

def imprimirDatosVehiculoBusqueda():
    for i in datosVehiculo:
        print(i)

def buscarVehiculo(indexPatente):
    for i in range(len(datosVehiculo)):
        for j in range(len(datosVehiculo[i])):
            if datosVehiculo[i][j] == indexPatente:
                return datosVehiculo[i]

def imprimirCertificado():
    if len(datosVehiculo) == 0:
        input("¡No existen datos aun!, Presione enter para continuar: ")
    else:
        print("#############################")
        print(f"Nombre certicado: AUTOSEGURO-R9")
        for i in datosVehiculo:
                print(f"Patente del auto: {i[1]}")
                print(f"Nombre del dueño: {i[6]}")
        print("#############################")
        
        input("Presione, enter para continuar: ")


while i:
    menu_Opcion = menu_general()

    match menu_Opcion:
        case 1:
            GuardarDatosVehiculo()
        case 2:
            imprimirDatosVehiculoBusqueda()
            print()

            datoBusqueda = input("Ingresa el vehiculo que desea encontrar: ")
            vehiculoEncontrado = buscarVehiculo(datoBusqueda)
            
            print()
            print(vehiculoEncontrado)
            print()
            input("¡El vahiculo se ha encontrado exitoamente!, presiona enter para continuar: ")

        case 3:
            imprimirCertificado()

        case 4:
            input("¡Vuelva pronto!, Precione enter para continuar: ")
            i = False
        case _:
            print("La opción elegida no es valida!")