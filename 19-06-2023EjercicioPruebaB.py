import os

persona = []

def MenuGeneral():
    os.system("cls")
    print("Bienvenidos al registro de NIF")
    print("1) Grabar", "2) Buscar", "3) Imprimir Certificado", "4) Salir", sep="\n")
    try:
        opcionElegida = int(input(""))
    except:
        return print("Error, al poder elegir una opción")