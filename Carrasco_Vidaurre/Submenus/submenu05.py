#programa para pedir el nombre de los trabajadores de una empresa(contratado o nombrado)

import libreria

max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Contratado")
    print("2: Nombrado")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.contratado()
    if(opc==2):
        libreria.nombrado()

    if (opc==3):

        if (libreria.mostrar_datos("Submenu5.txt")!=""):
            print(libreria.mostrar_datos("Submenu5.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu5.txt","","w")
