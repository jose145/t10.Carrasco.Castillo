# porgrama que pide correo electroco y guarda en una list
import libreria

max=3
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese Correo Electronico")
    print("2: Mostrar Datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))

    validar_opcion=libreria.validar_opcion(opc,1,2)

    lista=[]
    if(opc==1):
        correo=libreria.pedir_correo()
        lista.append(correo)

    for i in lista:
        libreria.agregar_datos("Menu4.txt","Correo: "+i,"w")
    if(opc==2):
        print("-->"+libreria.mostrar_datos("Menu4.txt"))

