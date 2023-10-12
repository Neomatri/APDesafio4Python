lista = [1, 2, 3, 4, 5, 6]
condicionalSi = ["SI", "Si", "sI", "si"] 

def agregarObjeto(): 
    agregar = input("¿Desea agregar o modificar un elemento a la lista? ")
    if (agregar in condicionalSi):
        agregado = input("¿Que desea agregar? ")
        agregadoPos = int(input("¿En que posicion? "))
        if (agregadoPos < 0 or agregadoPos > (len(lista) - 1)):
            print("Error: Escriba la posicion dentro de los limites.")
        elif (agregado.isalpha()): # Comprueba que se escriban letras
            lista.insert(agregadoPos, agregado) # Inserta en la lista los nuevos datos [Posicion, dato]
            print(f"Listo, ahora tu lista es {lista}")
        else:
            lista.insert(agregadoPos, int(agregado)) # Convierte los datos a números de la nueva lista
            print(f"Listo, ahora tu lista es {lista}")
    else:
        pass

agregarObjeto()

def eliminarObjeto():
    eliminar = input("¿Desea eliminar un item? ")
    if (eliminar in condicionalSi):
        elimarObjPos = int(input(f"Elija la posicion del objeto a eliminar entre 0 y {len(lista) - 1} ")) #Comprueba si se encuentra en el rango de la lista "{len(lista) - 1}" marca el ultimo objeto en la lista
        if(elimarObjPos < 0 or elimarObjPos > (len(lista) - 1)): #Comprueba si el valor introducido es distinto a los limites de la lista
            print("Escriba un numero entre los parametros dichos ")
        else:
            lista.pop(elimarObjPos) #Elimina el objeto en la posicion seleccionada
            print(f"Listo, ahora tu lista es {lista}")
    else:
        pass
        
eliminarObjeto()

while True:
    print("1. Agregar objeto")
    print("2. Eliminar objeto")
    print("3. Salir")
    opcion = input("Elegi una opción: ")

    if opcion == '1':
        agregarObjeto()
    elif opcion == '2':
        eliminarObjeto()
    elif opcion == '3':
        break
    else:
        print("Error, eliga una opcion")