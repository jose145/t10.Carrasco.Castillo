#programa para pedir operaciones (sumar y restar) de dos numero
#y de la respuesta

import libreria

max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Sumar")
    print("2: Restar")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.sumar()
    if(opc==2):
        libreria.restar()

    if (opc==3):

        if (libreria.mostrar_datos("Submenu7.txt")!=""):
            print(libreria.mostrar_datos("Submenu7.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu7.txt","","w")
