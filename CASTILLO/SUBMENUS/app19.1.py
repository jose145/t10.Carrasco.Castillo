import libreria2

def nuevoEstacion():
    opc=0
    max=3
    while ( opc != max ):
        print("############  NUEVA ESTACION  ############")
        print("# 1. Ingrese datos de la Nuevo Estacion  #")
        print("# 2. Mostrar datos de la Nuevo Estacion  #")
        print("# 3. Salir                               #")
        print("##########################################")

        opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
        if (opc==1):
            # 1. Pedir estacion
            # 2. Guardadr datod en info.txt
            estacion=libreria2.pedir_estacion("Ingrese estacion: ")
            numero= libreria2.pedir_numero("Ingrese numero; " , 1 , 4)
            contenido = estacion + "-" + str(numero) + "\n"
            libreria2.guardar_datos("app19.1.txt", contenido,"a")
            print("Estacion nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app19.1.txt")
            if ( datos != ""):
                for item in datos:
                    estacion, numero = item.split("-")
                    msg=" La estacion {} es la {} del anio"
                    estacion=estacion.replace("\n","")
                    numero= numero.replace("\n","")
                    print(msg.format(estacion, str(numero)))

            else:
                print("Archivo vacio")

def mostrarEstacion():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app19.1.txt")
    if ( datos != ""):
        for item in datos:
            estacion, numero = item.split("-")
            msg=" La estacion {} es la {} del anio"
            estacion=estacion.replace("\n","")
            numero= numero.replace("\n","")
            print(msg.format(estacion, str(numero)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Estacion         #")
    print("# 2. Mostrar Estacion       #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoEstacion()

    if (opc==2):
        mostrarEstacion()

print("Adios")
