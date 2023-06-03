import os
bucle = True
i = 1

def Menu():
    os.system('cls')
    print("----- Bienvenido al programa -----", "----- venta de servidores y hardware -----", sep="\n")
    print("1) Grabar", "2) Buscar", "3) Imprimir", "4) Salir", sep="\n")
    try:
        opcionElegida = int(input("Seleccione la opcion a elegir: "))
        return opcionElegida
    except:
        print("Error al escoger una opcion del menu :(")


def grabar():
    numeroPartesIngresadas = int(input("Cuantas partes desea ingresar del 1 al 10: "))
    if numeroPartesIngresadas > 0 and numeroPartesIngresadas < 11:
        while i == numeroPartesIngresadas:
            print()
            print(f"Numero de partes {i}")
            index = input("Ingrese su indice: ")
            servidor = input("Ingrese su servidor: ")
            modelo = input("Ingrese su modelo: ")

            numeroPartes = [index, servidor, modelo]
            i += 1

    else:
        print("El numero ingresado se pasa del rango")

OpcionElegidaMenu = Menu()

while bucle:
    match OpcionElegidaMenu:
        case 1:
            print("---- GRABAR ----")

            grabar()
        # case 2:

        # case 3:

        case 4:
            os.system('cls')
            print("Vuelva Pronto! :)")
            bucle = False

        case _:
            print("Opcion Elegida no valida")
            bucle = False



