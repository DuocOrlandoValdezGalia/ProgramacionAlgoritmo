def Suma(val1,val2):
    return val1+val2

def Resta(val1,val2):
    return val1-val2

def Multiplicacion(val1, val2):
    return val1*val2

def division(val1 , val2):
    return val1/val2

eleccion = ["1) Suma", "2) Resta", "3) Multiplicación", "4) Division"]

for i in eleccion:
    print(i)

opcionElegida = int(input("Ingrese la operacion que desee: "))

match opcionElegida:
    case 1:
        print("\n----------- SUMA -----------\n")        
        val1 = int(input("ingrese el primer valor: "))
        val2 = int(input("ingrese el segundo valor: "))

        print(f"Su resultado es: {Suma(val1, val2)}")
    case 2:
        print("\n----------- Resta -----------\n")        
        val1 = int(input("ingrese el primer valor: "))
        val2 = int(input("ingrese el segundo valor: "))

        print(f"Su resultado es: {Resta(val1, val2)}")

    case 3:
        print("\n ----------- Multiplicación -----------\n")        
        val1 = int(input("ingrese el primer valor: "))
        val2 = int(input("ingrese el segundo valor: "))

        print(f"Su resultado es: {Multiplicacion(val1, val2)}")

    case 4:
        print("\n----------- División -----------\n")        
        try:
            val1 = int(input("ingrese el primer valor: "))
            val2 = int(input("ingrese el segundo valor: "))

            print(f"Su resultado es: {division(val1, val2)}")

        except ZeroDivisionError:
            print("No puede dividir por 0")
    case _:
        print("Opcion elegida, no valida!")
    