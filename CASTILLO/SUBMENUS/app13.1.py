import libreria2

def nuevoTelf():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO TELEFONO  ###########")
        print("# 1. Ingrese datos del telefono       #")
        print("# 2. Mostrar datos del Telefono       #")
        print("# 3. Salir                            #")
        print("#######################################")
        opc= libreria2.pedir_numero("Ingrese opcion: ",1,3)

        if (opc==1):
            # 1. Pedir Telefono
            # 2. Pedir Empresa
            # 3. Guardadr datos en info.txt
            Telefono=libreria2.pedir_telf("Ingrese numero de telefono: ")
            Usuario=libreria2.pedir_nombre("Ingrese nombre de usuario: ")
            contenido = Usuario + "-" + str(Telefono) + "\n"
            libreria2.guardar_datos("app13.1.txt", contenido,"a")
            print("Telefono nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app13.txt")
            if ( datos != ""):
                for item in datos:
                    Telefono, Usuario= item.split("-")
                    msg=" El numero {} es de {} "
                    Telefono=Telefono.replace("\n","")
                    Usuario=Usuario.replace("\n","")
                    print(msg.format(Usuario, str(Telefono)))

            else:
                print("Archivo vacio")


def mostrarTelf():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app13.1.txt")
    if ( datos != ""):
        for item in datos:
            Telefono, Usuario= item.split("-")
            msg=" El numero {} es de {} "
            Telefono=Telefono.replace("\n","")
            Usuario=Usuario.replace("\n","")
            print(msg.format(Usuario, str(Telefono)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Telefono           #")
    print("# 2. Mostrar Telefono         #")
    print("# 3. Salir                    #")
    print("#############################")
    opc= libreria2.pedir_numero("Ingrese opcion: ",1,3)

    if (opc==1):
        nuevoTelf()

    if (opc==2):
        mostrarTelf()

print("Adios")
