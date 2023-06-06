import os
cafes = ["Expresso", "Capuchino", "Latte", "Moca"]
precioCafe = [1500, 1800, 1600, 1700]
acExpreso = 0
acCapuchino = 0
acLatte = 0
acMoca = 0

sbExpreso = 0
sbCapuchino = 0
sbLatte = 0
sbMoca = 0

i = True

def MenuCafes():
    print("Seleccion de cafes: ", f"1) {cafes[0]} - ${precioCafe[0]}", f"2) {cafes[1]} - ${precioCafe[1]}", f"3) {cafes[2]} - ${precioCafe[2]}", f"4) {cafes[len(cafes) - 1]} - ${precioCafe[len(precioCafe) - 1]}", "5) Salir", sep="\n")
    try:
        opcionElegida = int(input("Eliga un cafe: "))
        return opcionElegida
    except:
        print("Ha ocurrido un error en su elección")

def factura( subtotalExpreso, subtotalCapuchino, subtotalLatte, subtotalMoca ):
    print("==================== Boleta ====================")
    print(f"{acExpreso} Expreso - ${subtotalExpreso}", f"{acCapuchino} Capuchino - ${subtotalCapuchino}", f"", f"",)

while i:
    opcionElegida = MenuCafes()
    
    match opcionElegida:
        case 1:
            acExpreso += 1
            sbExpreso = acExpreso * precioCafe[0]
            print("\nSe ha agregado correctamente!\n")

        case 2:
            acCapuchino += 1
            sbCapuchino = acCapuchino * precioCafe[1]
            print("\nSe ha agregado correctamente!\n")

        case 3:
            acLatte += 1
            sbLatte = acLatte * precioCafe[2]
            print("\nSe ha agregado correctamente!\n")

        case 4:
            acMoca += 1
            sbMoca = acMoca * precioCafe[len(cafes) - 1]
            print("\nSe ha agregado correctamente!\n")

        case 5: 
            os.system("cls")
            print("Vuelva Pronto! :)")
            i = False

        case _:
            print("\n6Opcion elegida no valida!\n")