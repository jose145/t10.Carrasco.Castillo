import libreria2

def nuevoDNI():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO DNI  ###########")
        print("# 1. Ingrese datos del Nuevo DNI #")
        print("# 2. Mostrar datos del Nuevo DNI #")
        print("# 3. Salir                       #")
        print("##################################")

        opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
        if (opc==1):
            # 1. Pedir DNI
            # 2. Pedir nombre
            # 3. Guardar datos en info.txt
            DNI=libreria2.pedir_DNI("Ingrese numero de DNI: ")
            nombre=libreria2.pedir_nombre("Ingrese nombre: ")
            contenido = nombre + "-" + str(DNI) + "\n"
            libreria2.guardar_datos("app14.1.txt", contenido,"a")
            print("DNI nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app14.1.txt")
            if ( datos != ""):
                for item in datos:
                    nombre, DNI= item.split("-")
                    msg=" El alumno es {} y su DNI es {} "
                    nombre=nombre.replace("\n","")
                    DNI=DNI.replace("\n","")
                    print(msg.format(nombre, str(DNI)))

            else:
                print("Archivo vacio")

def mostrarDNI():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app14.1.txt")
    if ( datos != ""):
        for item in datos:
            nombre, DNI= item.split("-")
            msg=" El alumno es {} y su DNI es {} "
            nombre=nombre.replace("\n","")
            DNI=DNI.replace("\n","")
            print(msg.format(nombre, str(DNI)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo DNI           #")
    print("# 2. Mostrar DNI         #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoDNI()

    if (opc==2):
        mostrarDNI()

print("Adios")
