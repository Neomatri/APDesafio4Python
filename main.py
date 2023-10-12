lista = [1, 2, 3, 4, 5, 6]
condicionalSi = ["SI", "Si", "sI", "si"] 
condicionalNum = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

def agregarObjeto(): 
    agregar = input("¿Desea agregar o modificar un elemento a la lista? ")
    if (agregar in condicionalSi): #comprueba si el valor ingresado esta en la lista "condicionalSi"
        agregado = input("¿Que desea agregar? ")
        agregadoPos = input("¿En que posicion? ")
        if (agregado.isalpha): # Comprueba que se escriban letras
            lista.insert(int(agregadoPos), agregado) #Inserta en la lista los nuevos datos [Posicion, dato]
            print(f"Listo, ahora tu lista es {lista}")
        else:
            lista[int(agregadoPos)] = int(agregado) #Convierte los datos a numeros de la nueva lista
            print(f"Listo, ahora tu lista es {lista}")
    else:
        pass

agregarObjeto() 

def eliminarObjeto():
    eliminar = input("¿Desea eliminar un item? ")
    if (eliminar in condicionalSi):
        elimarObjPos = int(input(f"Elija la posicion del objeto a eliminar entre 0 y {len(lista) - 1} ")) #Comprueba si se encuentra en el rango de la lista "{len(lista) - 1}" marca el ultimo objeto en la listano
        if(elimarObjPos < 0 or elimarObjPos > len(lista) - 1): #Comprueba si el valor introducido es distinto a los limites de la lista
            print("Escriba un numero entre los parametros dichos ")
        else:
            lista.pop(elimarObjPos)
            print(f"Listo, ahora tu lista es {lista}")
    else:
        pass
        
eliminarObjeto()

while True:
    print("\n1. Agregar objeto")
    print("2. Eliminar objeto")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        agregarObjeto()
    elif opcion == '2':
        eliminarObjeto()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")