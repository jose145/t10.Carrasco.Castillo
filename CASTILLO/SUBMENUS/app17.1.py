import libreria2

def nuevoTalla():
    opc=0
    max=3
    while ( opc != max ):
        print("############# NUEVA TALLA  #############")
        print("# 1. Ingrese datos de la Nuevo Talla   #")
        print("# 2. Mostrar datos de la Nuevo Talla   #")
        print("# 3. Salir                             #")
        print("########################################")

        opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
        if (opc==1):
            # 1. Pedir Talla
            # 2. Pedir Persona
            # 3. Guardadr datos en info.txt
            talla=libreria2.pedir_talla("Ingrese Talla: ")
            persona=libreria2.pedir_nombre("Ingrese Nombre: ")
            contenido = persona + "-" + str(talla) + "\n"
            libreria2.guardar_datos("app17.1.txt", contenido,"a")
            print("Talla nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app17.1.txt")
            if ( datos != ""):
                for item in datos:
                    persona, talla= item.split("-")
                    msg= "La persona es {} y su talla es {}m"
                    persona=persona.replace("\n","")
                    talla= talla.replace("\n","")
                    print(msg.format(persona, str(talla)))

            else:
                print("Archivo vacio")

def mostrarTalla():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app17.1.txt")
    if ( datos != ""):
        for item in datos:
            persona, talla= item.split("-")
            msg= "La persona es {} y su talla es {}m"
            persona=persona.replace("\n","")
            talla= talla.replace("\n","")
            print(msg.format(persona, str(talla)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Talla            #")
    print("# 2. Mostrar Talla          #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoTalla()

    if (opc==2):
        mostrarTalla()

print("Adios")
