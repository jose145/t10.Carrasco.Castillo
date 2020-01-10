#programa para pedir edad y el dni
import libreria

max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Menor de edad")
    print("2: Aldulto")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.menor()
    if(opc==2):
        libreria.adulto()

    if (opc==3):

        if (libreria.mostrar_datos("Submenu3.txt")!=""):
            print(libreria.mostrar_datos("Submenu3.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu3.txt","","w")
