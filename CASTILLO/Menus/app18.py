import libreria

def nuevoCodigo():
    # 1. Pedir nombre
    # 2. Pedir codigo
    # 3. Guardadr datod en info.txt
    nombre=libreria.pedir_nombre("Ingrese nombre: ")
    codigo=libreria.pedir_codigo("Ingrese codigo: " )
    contenido = nombre + "-" + str(codigo) + "\n"
    libreria.guardar_datos("app18.txt", contenido,"a")
    print("Codigo nuevo guardado")

def mostrarCodigo():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app18.txt")
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

    opc= libreria.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoCodigo()

    if (opc==2):
        mostrarCodigo()

print("Adios")





