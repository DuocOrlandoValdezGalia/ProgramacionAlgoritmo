persona = ['2-8','Orlando','Valdez', 'Fuerte']

grupo = [
    ['2-8','Orlando','Valdez', 'Fuerte'],
    ['31-8','Maria','lopez', 'Delgada'],
    ['53-8','Juana','Carns', 'vieja']
]

# for i in range(len(persona)):
#     if i == 1:
#         print(persona[i])

for i in range(len(persona)):
    for j in range(len(grupo)):
        if i == 0:
            print(grupo[j][i])

def busquedaPorRut(rut_persona):
    for i in range(len(grupo)):
        for j in range(len(grupo[i])):
            if grupo[i][j] == rut_persona:
                return grupo[i]

print(busquedaPorRut("Maria"))
print()

def imprimir_Persona(arraypersona):
    print(f"RUT:      \t\t {arraypersona[0]}")
    print(f"Nombre:   \t\t {arraypersona[1]}")
    print(f"Apellido: \t\t {arraypersona[2]}")
    print(f"Prototipo:\t\t  {arraypersona[3]}")

busqueda = input("Ingrese lo que desea buscar: ")

print(imprimir_Persona(busquedaPorRut(busqueda)))
    
    





