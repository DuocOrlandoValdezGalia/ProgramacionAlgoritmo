from ast import Str
from operator import truediv
from tkinter import CENTER
import os
from wsgiref.validate import InputWrapper

nombreAgencia = "Auto Seguro"
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
            return Str(precio)
        else:
            input("Error al guardar la precio, precione enter para continuar: ")

def GuardarDatosVehiculo():
    tipo = input("Tipo: ")
    patente = ValidarPatente()
    marca = ValidarMarca()
    precio = ValidarPrecio() 
    multas = input("Multas: ") 
    fechaRegistro = input("Fecha Registro: ") 
    nombreDueno = input("Nombre Dueno: ") 




while i:
    menu_Opcion = menu_general()

    match menu_Opcion:
        case 1:
            GuardarDatosVehiculo()

        case _:
            print("La opción elegida no es valida!")