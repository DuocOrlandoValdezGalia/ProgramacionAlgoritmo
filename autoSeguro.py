datosVehiculo = []
i = True
nombre = ""
apellido = ""

def menu():  
    
    print("\nBIENVENIDOS A AUTO SEGURO\n")
          
    print("1) Grabar", "2) Buscar", "3) Imprimir certificados", "4) Salir", sep="\n")
    try: 
        opcionElegida = int(input("Ingrese un valor: "))
        return opcionElegida
    except: 
        print("Error al elegir una opcion")
        

def grabar():
    tipo = input("\nIngrese el tipo de vehiculo: ")
    patente = input("Ingrese la patente del vehiculo: ")
    marca = input("Ingresa la marca del vehiculo: ")
    if len(marca) >= 2 and len(marca) <= 15:
        marca = marca
    else:
        print("La marca necesita de 3 a 15 caracteres")
        marca = input("Ingresa la marca del vehiculo: ")
        if len(marca) < 2 and len(marca) > 15:
            return print("Error al ingresar una marca")
        
    precioVehiculo = int(input("Ingresa el precio del vehiculo: "))
    if precioVehiculo < 5000000:
        print("El precio no puede ser menor a $5.000.000")
        precioVehiculo = int(input("Ingresa el precio del vehiculo: "))
        
        if precioVehiculo < 5000000:
            return print("Error al ingresar una precio")
    multas = int(input("Ingrese la cantidad de multas: "))
    fechaDeRegistro = input("Ingresa la fecha de registro del vehiculo: ")
    dueno = input("Ingresa el nombre del dueño: ")   
    
    datosVehiculo.append([tipo, patente, marca, precioVehiculo, multas, fechaDeRegistro, dueno]) 
    print("\n¡Se han guardado los datos del vehiculo satisfactoriamente!\n")
    
def buscarVehiculo(index): 
    for i in range(len(datosVehiculo)):
        for j in range(len(datosVehiculo[i])):
            if datosVehiculo[i][j] == index:
                return datosVehiculo[i] 
            
def imprimir(datos): 
    print("")
    print(f"Tipo: {datos[0]}")
    print(f"Patente: {datos[1]}")
    print(f"Marca: {datos[2]}")
    print(f"Precio: ${datos[3]}")
    print(f"Cantidad de Multas: {datos[4]}")
    print(f"Fecha de registro: {datos[5]}")
    print(f"Nombre del dueño: {datos[len(datos) - 1]}")
   
while i:
    
    opcionElegida = menu()
    
    match opcionElegida:
        
        case 1:
            grabar()
        
        case 2:
            if len(datosVehiculo) > 0:
                for i in datosVehiculo:
                    print([i])
                    
                patente = input("Ingrese la patente del vehiculo a buscar: ")
                vehiculoEncontrado = buscarVehiculo(patente)
                imprimir(vehiculoEncontrado)
            else:
                print("No se encuentran datos registrados!")
                input()
        
        case 4:
            print(f"Vuelva pronto! {nombre} {apellido}")
            i = False
        
        case _:
            print("Opcion elegida no valida.")