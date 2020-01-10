import libreria

#programa que pide nombre valido
max=3
opc=0
while(opc!=max ):
    #mostrar menu de opciones
    print("1: Ingrese Nombre")
    print("2: Mostrar Datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))

    validar_opcion=libreria.validar_opcion(opc,1,2)

    lista=[]

    #si se ingresa la opc 1 pedira el nombre
    if(opc==1):
        nombre=libreria.pedir_nombre()
        print("Dato guardado")
        lista.append(nombre)

    for i in lista:
        libreria.agregar_datos("Menu1.txt","Nombre: "+i,"w")


    #si ingresa la opc 2, mostrara los datos
    if(opc==2):
        datos=libreria.mostrar_datos("Menu1.txt")
        print("->"+datos)

#fin while

