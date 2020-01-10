#programa para pedir el nombre y su facultad
import libreria

max=3
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese datos del estudiante")
    print("2: Mostar datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,2)


    if(opc==1):
        libreria.estudiante()

    if (opc==2):

        if (libreria.mostrar_datos("Submenu4.txt")!=""):
            print(libreria.mostrar_datos("Submenu4.txt"))

        else:
            print("Archivo Vacio")
if(opc==3):
    libreria.agregar_datos("Submenu4.txt","","w")
