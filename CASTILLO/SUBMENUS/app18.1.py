import libreria2

def nuevoCodigo():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO CODIGO  ###########")
        print("# 1. Ingrese datos del nuevo Codigo #")
        print("# 2. Mostrar datos del nuevo Codigo #")
        print("# 3. Salir                          #")
        print("#####################################")

        opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
        if (opc==1):
            # 1. Pedir nombre
            # 2. Pedir codigo
            # 3. Guardadr datod en info.txt
            nombre=libreria2.pedir_nombre("Ingrese nombre: ")
            codigo=libreria2.pedir_codigo("Ingrese codigo: " )
            contenido = nombre + "-" + str(codigo) + "\n"
            libreria2.guardar_datos("app18.1.txt", contenido,"a")
            print("Codigo nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app18.1.txt")
            if ( datos != ""):
                for item in datos:
                    nombre, codigo= item.split("-")
                    msg=" El alumno es {} y su codigo es {}"
                    nombre=nombre.replace("\n","")
                    codigo=codigo.replace("\n","")
                    print(msg.format(nombre, codigo))

        else:
            print("Archivo vacio")

def mostrarCodigo():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app18.1.txt")
    if ( datos != ""):
        for item in datos:
            nombre, codigo= item.split("-")
            msg=" El alumno es {} y su codigo es {}"
            nombre=nombre.replace("\n","")
            codigo=codigo.replace("\n","")
            print(msg.format(nombre, codigo))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Codigo           #")
    print("# 2. Mostrar Codigo         #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoCodigo()

    if (opc==2):
        mostrarCodigo()

print("Adios")





