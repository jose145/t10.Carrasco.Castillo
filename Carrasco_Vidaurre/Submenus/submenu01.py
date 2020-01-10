import libreria

#programa que me pide datos de alumnos de universidad Nacional y Particular
max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Alumno de Universaidad Nacional")
    print("2: Alumno de Universaidad Particular")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)


    if(opc==1):
        libreria.alumno_nacional()
    if(opc==2):
        libreria.alumno_particular()

    if (opc==3):

        if (libreria.mostrar_datos("Submenu1.txt")!=""):
            print(libreria.mostrar_datos("Submenu1.txt"))

        else:
            print("Archivo Vacio")
if(opc==4):
    libreria.agregar_datos("Submenu1.txt","","w")
