import libreria

def nuevoPrecio():
    # 1. Pedir Precio
    # 2. Pedir Producto
    # 3. Guardadr datos en info.txt
    Precio=libreria.pedir_real("Ingrese Precio: ")
    Producto=libreria.pedir_nombre("Ingrese Producto: ")
    contenido = Producto + "-" + str(Precio) + "\n"
    libreria.guardar_datos("app15.txt", contenido,"a")
    print("Producto nuevo guardado")

def mostrarPrecio():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app15.txt")
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

    opc= libreria.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoPrecio()

    if (opc==2):
        mostrarPrecio()

print("Adios")
