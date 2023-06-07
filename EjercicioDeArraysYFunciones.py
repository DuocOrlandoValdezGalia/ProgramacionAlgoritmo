import os
bucle = True
i = 0
partes = []

print("----- Bienvenido al programa -----", "----- venta de servidores y hardware -----", sep="\n")

def Menu():
    print("1) Grabar", "2) Buscar", "3) Imprimir", "4) Salir", sep="\n")
    try:
        opcionElegida = int(input("Seleccione la opcion a elegir: "))
        return opcionElegida
    except:
        print("Error al escoger una opcion del menu :(")


def grabar():
    numeroPartesIngresadas = int(input("Cuantas partes desea ingresar del 1 al 10: "))
    if numeroPartesIngresadas > 0 and numeroPartesIngresadas < 11:
        i = 1
        while i <= numeroPartesIngresadas:
            print()
            print(f"Numero de partes {i}")
            index = input("Ingrese su indice: ")
            servidor = input("Ingrese su servidor: ")
            precioProducto = int(input("Ingrese su precio del producto: "))

            if precioProducto == 0:
                precioProducto = 1
            
            partesCompleto = [index, servidor, precioProducto]
            partes.append(partesCompleto)
            i += 1

        return partes
    else:
        print("El numero ingresado se pasa del rango")

def buscar(ParteABuscar):
    for i in range(len(partes)):
        for j in range(len(partes[i])):
            if partes[i][j] == ParteABuscar:
                return partes[i]
        
    
while bucle:
    OpcionElegidaMenu = Menu()
    
    match OpcionElegidaMenu:
        case 1:
            print("---------------- GRABAR ----------------")

            numeroPartesGuardadas = grabar()
            print("Se ha guardado la cantidad de partes exitosamente!\n")
            
        case 2:
            print("---------------- Buscar ----------------")
            print("Registros existentes: ")
            if len(partes) > 0:
                print(partes)
                
                print("\nPuede filtrar por el campo que desee!")
                filtro = input("Ingrese un valor a filtrar: ")
                registroEncontrado = buscar(filtro)
                precioProductoidentificador = registroEncontrado[ len(registroEncontrado) - 1 ]
                
                if precioProductoidentificador > 500:
                    print(f"\nNumero de parte: {registroEncontrado[0]}")
                    print(f"Nombre Producto: {registroEncontrado[1]}")
                    print(f"Precio Producto: ${registroEncontrado[ len(registroEncontrado) - 1 ]}\n")
                else:
                    print("Sin stock!")
                
            else:
                print("No se encuentra ningun registro existente.", f"{partes}\n", sep="\n")
        # case 3:

        case 4:
            os.system('cls')
            print("Vuelva Pronto! :)")
            bucle = False

        case _:
            print("Opcion Elegida no valida")
            bucle = False



