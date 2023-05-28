i = True
acumuladorPeperoni = 0
acumuladorMargarita = 0
acumuladorBarbacoa = 0

subTotalPeperoni = 0
subTotalMargarita = 0
subTotalBarbacoa = 0

descuento = 0
subTotal = 0
total = 0

def facturacion(acumuladorP, acumuladorM, acumuladorB, subtotalP, subTotalM, subTotalB):
    subTotal = subtotalP + subTotalM + subTotalB
    
    # Impresion Boleta #
    print("============ Boleta ============")
    print(f"{acumuladorP} Pizzas peperoni - ${subtotalP}", 
          f"{acumuladorM} Pizzas margarita - ${subTotalM}", 
          f"{acumuladorB} Pizzas barbacoa - ${subTotalB}", sep="\n")
    print("================================")
    print(f"Subtotal - ${subTotal}")
    if subTotal > 10000:
        descuento = subTotal * 10 / 100
        total = subTotal - descuento
        print(f"Descuento - ${descuento}")
    else:
        total = subTotal
        print("Usted no cuenta con descuento.")
    print("================================")
    print(f"Total - ${total}")
    print()
    print("Gracias por su compra! vuelva pronto :)")


def Menu1():
    print("\n============ Pizzas ============\n")
    print("1) Pizza Peperoni - $7000", "2) Margarita - $5000", "3) Barbacoa - $10000\n", sep="\n")
    pizzaElegida = int(input("Elija una opción: "))

    if pizzaElegida > 0 and pizzaElegida < 4:
        return pizzaElegida
    else:
        return print("Opción elegida, no valida!")

while i:
    pizzaElegida = Menu1()

    match pizzaElegida:
        case 1:
            precio = 7000
            cantidadPizzasPeperoni = int(input("Cuantas pizzas de peperoni desea: "))
            acumuladorPeperoni += cantidadPizzasPeperoni
            if acumuladorPeperoni > 0:
                print("Desea mas de peperoni?", "1) Si", "2) No\n", sep="\n")
                deseaMas = int(input("Ingrese una opción: "))

                if deseaMas == 1:
                    cantidadPizzasPeperoni = int(input("Cuantas pizzas de peperoni desea: "))
                    acumuladorPeperoni += cantidadPizzasPeperoni
                    
            subTotalPeperoni = precio * acumuladorPeperoni            
        case 2:
            precio = 5000
            cantidadPizzasMargarita = int(input("Cuantas pizzas de margarita desea: "))
            acumuladorMargarita += cantidadPizzasMargarita
            if acumuladorMargarita > 0:
                print("Desea mas de margarita?", "1) Si", "2) No\n", sep="\n")
                deseaMas = int(input("Ingrese una opción: "))

                if deseaMas == 1:
                    cantidadPizzasMargarita = int(input("Cuantas pizzas de margarita desea: "))
                    acumuladorMargarita += cantidadPizzasMargarita 
                    
            subTotalMargarita = precio * acumuladorMargarita   
        case 3:
            precio = 10000
            cantidadPizzasBarbacoa = int(input("Cuantas pizzas de barbacoa desea: "))
            acumuladorBarbacoa += cantidadPizzasBarbacoa
            if acumuladorBarbacoa > 0:
                print("Desea mas de barbacoa?", "1) Si", "2) No\n", sep="\n")
                deseaMas = int(input("Ingrese una opción: "))

                if deseaMas == 1:
                    cantidadPizzasBarbacoa = int(input("Cuantas pizzas de barbacoa desea: "))
                    acumuladorBarbacoa += cantidadPizzasBarbacoa
            
            subTotalBarbacoa = precio * acumuladorBarbacoa  
        case _:
            print("La opción elegida, no es valida!")
            
    print("Desea imprimir la boleta?", "1) Si", "2) No\n", sep="\n")
    impresionBoleta = int(input("Escoja una opción: "))
    
    if impresionBoleta == 1:
        if acumuladorBarbacoa > 0 or acumuladorMargarita > 0 or acumuladorPeperoni > 0:
            facturacion(acumuladorPeperoni, acumuladorMargarita, acumuladorBarbacoa, subTotalPeperoni, subTotalMargarita, subTotalBarbacoa)
            i = False
        else:
            print("No tiene ninguna pizza elegida, Vuelva a escoger.")

    