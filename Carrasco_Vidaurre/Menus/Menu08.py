import libreria

max=3
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese Mes")
    print("2: Mostrar Datos")
    print("3: Salir")
    opc=int(input("Ingrese opcion:"))

    validar_opcion=libreria.validar_opcion(opc,1,2)

    lista=[]
    if(opc==1):
        mes=libreria.pedir_mes()
        lista.append(mes)

    for i in lista:
        libreria.agregar_datos("Menu8.txt","Mes: "+i,"w")
    if(opc==2):
        print("-->"+libreria.mostrar_datos("Menu8.txt"))
