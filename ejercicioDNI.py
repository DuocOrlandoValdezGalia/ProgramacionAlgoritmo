import os
i = True
persona = []


def MenuGeneral():
    os.system("cls")
    print("\n######################################", "### Bienvenidos al registro de NIF ###", "######################################\n", sep="\n")
    print("1) Grabar", "2) Buscar", "3) Imprimir certificado", "4) Salir\n", sep="\n")
    try:
        opcionElegida = int(input("Escoja una de las opciones: "))
        return opcionElegida
    except:
        input("Ha ocurrido un error al escoger una opción, presione enter para continuar: ")
    
    
def EdadVerificada():
    edadVerificada = True
    while edadVerificada:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad >= 0:
                edadVerificada = False
                return edad
        except:
            input("Ha ocurrido un error, presione enter para continuar: ")
            
def NombreVerificado():
    nombreVerificado = True
    
    while nombreVerificado:
        try:
            nombre = input("Ingrese su nombre: ")
            if len(nombre) > 7:
                nombreVerificado = False
                return nombre
            else:
                input("El nombre debe tener 8 letras, presione enter para continuar: ")
        except:
            input("Ha ocurrido un error, presione enter para continuar: ")

def verificacionNumerosNif():
    verificacionNumerosNif = True
    while verificacionNumerosNif:
        try:
            numerosNIF = input("Ingrese los primeros numeros de su NIF: ")
            
            if len(numerosNIF) == 8:
                verificacionNumerosNif = False
                return numerosNIF
            elif len(numerosNIF) < 8: 
                input("El nif debe tener 8 digitos al comienzo, presione enter para continuar: ")
            elif len(numerosNIF) > 8: 
                input("El nif no puede tener mas de 8 digitos al comienzo, presione enter para continuar: ")
        except:
            input("Ha ocurrido un error, presione enter para continuar: ")
            
def verificarNif():
    verificarNif = True
    while verificarNif:
        try:
            LetrasNifGuion = "-"
            LetrasNif = input("Ingrese las Letras de su NIF: ")
            
            if len(LetrasNif) == 3:
                verificarNif = False
                LetrasNifGuion += LetrasNif
                return LetrasNifGuion
            elif len(LetrasNif) < 3:
                input("El nif debe tener 3 letras al final, presione enter para continuar: ")
            elif len(LetrasNif) > 3:
                input("El nif no puede tener mas de 3 letras al final, presione enter para continuar: ")
        except:
            input("Ha ocurrido un error, presione enter para continuar: ")
            
def NifVerificado():
    nifVerificado = True
    
    while nifVerificado:
        try:
            numerosNIF = verificacionNumerosNif()
            LetrasNIF = verificarNif()
            
            if numerosNIF != "" and LetrasNIF != "":
                NifCompleto = numerosNIF+LetrasNIF
                return NifCompleto
        except:
            input("Ha ocurrido un error, presione enter para continuar: ")

def GrabarPersona():
    nif = NifVerificado()
    nombre = NombreVerificado()
    edad = EdadVerificada()
    
    if nif != None and nombre != None and edad != None:
        persona.append([nif, nombre, edad])
    
def buscadorNIF(indexNIF):
    for i in range(len(persona)):
        for j in range(len(persona[i])):
            if persona[i][j] == indexNIF:
                return persona[i]

def mostrarRegistros():
    for i in persona:
        print(i)
  
def ImpresionCertidicado(persona):
    print("\n####################", "### CERTIFICADOS ###", "####################\n", sep="\n")
    print("1) Certificado de nacimiento", "2) Estado Conyugal", "3) Permanencia Union Europea", sep="\n")
    try:
        opcionElegidaCentificado = int(input("Escoja un certificado: "))
        certificado = True
        
        while certificado:
            match opcionElegidaCentificado:
                case 1:
                    print(f"Nombre Certificado: Certificado de nacimiento")
                    print(f"NIF: {persona[0]}")
                    print(f"Nombre: {persona[1]}")
                    print(f"Edad: {persona[2]}")
                    input("Su Certificado se ha impreso, correctamente!, presione enter para continuar: ")
                    certificado = False
                case 2:
                    print(f"Nombre Certificado: Estado Conyugal")
                    print(f"NIF: {persona[0]}")
                    print(f"Nombre: {persona[1]}")
                    print(f"Edad: {persona[2]}")
                    input("Su Certificado se ha impreso, correctamente!, presione enter para continuar: ")
                    certificado = False
                case 3:
                    print(f"Nombre Certificado: Permanencia Union Europea")
                    print(f"NIF: {persona[0]}")
                    print(f"Nombre: {persona[1]}")
                    print(f"Edad: {persona[2]}")
                    input("Su Certificado se ha impreso, correctamente!, presione enter para continuar: ")
                    certificado = False
                case _:
                    input("Opcion elegida, no esta dentro del rango. Presione enter para continuar: ")  
    except:
        input("Ha ocurrido un error, presione enter para continuar: ")
    
  
while i:
    opcionEscogida = MenuGeneral()
    match opcionEscogida:
        case 1: 
            GrabarPersona()
            
        case 2:
            print("--- Personas Regitradas ---")
            mostrarRegistros()
            buscarPersona = input("\nIngrese el nif de la persona a buscar: ")
            personaEncontrada = buscadorNIF(buscarPersona)
            if personaEncontrada != None:
                print(f"{personaEncontrada}")
                input("Registro Encontrado!, presione enter para continuar: ")
            else:
                input("Persona no encontrada!... Presione enter para continuar: ")
        
        case 3:
            os.system("cls")
            impresion = True
            
            while impresion:
                print("--- Personas Regitradas ---")
                mostrarRegistros()
                buscarPersona = input("\nIngrese el nif de la persona a imprimir certificado: ")
                personaEncontrada = buscadorNIF(buscarPersona)
                
                if personaEncontrada != None:
                    print("Desea imprimir resultados de la persona encontrada?", "1) Si", "2) No\n", sep="\n")
                    deseaImpresion = int(input("Eliga una opción: "))
                    
                    if deseaImpresion == 1:
                        
                        ImpresionCertidicado(personaEncontrada)
                        impresion = False
                    else:
                        input("Presiona enter para continuar: ")
                else:
                    input("Error al buscar persona, presione enter para continuar: ")
                
        
        case 4: 
            input("\nVuelva pronto!, presione enter para continuar: ")
            i = False
        case _:
            input("Opcion elegida, no esta dentro del rango. Presione enter para continuar: ")