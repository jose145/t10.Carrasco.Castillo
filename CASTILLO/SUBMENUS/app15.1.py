import libreria2

def nuevoPrecio():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO PRECIO  ###########")
        print("# 1. Ingrese datos del nuevo precio #")
        print("# 2. Mostrar datos del nuevo precio #")
        print("# 3. Salir                          #")
        print("#####################################")

        opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
        if (opc==1):
            # 1. Pedir Precio
            # 2. Pedir Producto
            # 3. Guardadr datos en info.txt
            Precio=libreria2.pedir_real("Ingrese Precio: ")
            Producto=libreria2.pedir_nombre("Ingrese Producto: ")
            contenido = Producto + "-" + str(Precio) + "\n"
            libreria2.guardar_datos("app15.1.txt", contenido,"a")
            print("Producto nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app15.1.txt")
            if ( datos != ""):
                for item in datos:
                    Producto, Precio= item.split("-")
                    msg=" El  producto es {} y cuesta S/. {} "
                    Producto=Producto.replace("\n","")
                    Precio=Precio.replace("\n","")
                    print(msg.format(Producto, str(Precio)))

            else:
                print("Archivo vacio")


def mostrarPrecio():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app15.1.txt")
    if ( datos != ""):
        for item in datos:
            Producto, Precio= item.split("-")
            msg=" El  producto es {} y cuesta S/. {} "
            Producto=Producto.replace("\n","")
            Precio=Precio.replace("\n","")
            print(msg.format(Producto, str(Precio)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Precio           #")
    print("# 2. Mostrar Precio         #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoPrecio()

    if (opc==2):
        mostrarPrecio()

print("Adios")
