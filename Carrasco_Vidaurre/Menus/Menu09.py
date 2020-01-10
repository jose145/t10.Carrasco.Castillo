import libreria

#programa que guarda datos como el asiento del bus,nombre y el dni
max=5
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese Nombre")
    print("2: Ingrese DNI")
    print("3: Ingrese asiento del bus")
    print("4: Mostrar Datos")
    print("5: Salir")
    opc=int(input("Ingrese opcion:"))

    validar_opcion=libreria.validar_opcion(opc,1,4)

    lista=[]
    if(opc==1):
        nombre=libreria.pedir_nombre()
        lista.append(nombre)

    if(opc==2):
        dni=libreria.pedir_dni()
        lista.append(dni)

    if(opc==3):
        asiento=libreria.pedir_asiento()
        lista.append(asiento)

    for i in lista:
        if(isinstance(i,str)):
            libreria.agregar_datos("Menu9.txt","Nombre: "+i +"\n","w")
        if (len(str(i))==8):
            libreria.agregar_datos("Menu9.txt","-->DNI: "+str(i)+"\n","a")
        if (len(str(i))==1 or len(str(i))==2 ):
            libreria.agregar_datos("Menu9.txt","-->Asiento: "+str(i),"a")

    if(opc==4):
        print("-->"+libreria.mostrar_datos("Menu9.txt"))
