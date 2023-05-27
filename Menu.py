i = True
acumuladorPeperoni = 1
acumuladorMargarita = 1
acumuladorBarbacoa = 1


def Menu1():
    print("============ Pizzas ============")
    print("1) Pizza Peperoni - $7000", "2) Margarita - $5000", "3) Barbacoa - $10000", sep="\n")
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
                print("Desea mas de peperoni?", "1) Si", "2) No", sep="\n")
                deseaMas = int(input("Ingrese una opción: "))

                if deseaMas == 1:
                    cantidadPizzasPeperoni = int(input("Cuantas pizzas de peperoni desea: "))
                    acumuladorPeperoni += cantidadPizzasPeperoni            

        # case 2:
        # case 3:
        case _:
            print("La opción elegida, no es valida!")

    