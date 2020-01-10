import libreria
#programa para pesir el nombre del postulante y mostrar el costo del su examen
#dependiendo del tipo de colegio
max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese datos del postulante")
    print("2: Mostar datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.postulante()
    if (opc==2):

        if (libreria.mostrar_datos("Submenu8.txt")!=""):
            print(libreria.mostrar_datos("Submenu8.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu8.txt","","w")
