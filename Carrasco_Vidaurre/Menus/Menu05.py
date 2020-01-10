#programa guarda el codigo universitario
import libreria

max=3
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese Codigo")
    print("2: Mostrar Datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))

    validar_opcion=libreria.validar_opcion(opc,1,2)

    lista=[]
    if(opc==1):
        codigo=libreria.pedir_codigo()
        lista.append(codigo)

    for i in lista:
        libreria.agregar_datos("Menu5.txt","Codigo: "+i,"w")
    if(opc==2):
        print("-->"+libreria.mostrar_datos("Menu5.txt"))
