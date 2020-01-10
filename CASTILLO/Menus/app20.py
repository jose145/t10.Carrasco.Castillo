import libreria

def nuevoPecado():
    # 1. Pedir nombre
    # 2. Pedir pecado
    # 3. Guardadr datod en info.txt
    nombre=libreria.pedir_nombre("Ingrese nombre: ")
    pecado=libreria.pedir_pecado("Ingrese pecado: " )
    contenido = nombre + "-" + str(pecado) + "\n"
    libreria.guardar_datos("app20.txt", contenido,"a")
    print("Pecado nuevo guardado")

def mostrarPecado():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app20.txt")
    if ( datos != ""):
        for item in datos:
            nombre, pecado= item.split("-")
            msg= "La persona {} tiene el pecado de {}"
            nombre=nombre.replace("\n","")
            pecado= pecado.replace("\n","")
            print(msg.format(nombre, pecado))

    else:
        print("Archivo vacio")
opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Pecado           #")
    print("# 2. Mostrar Pecado         #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoPecado()

    if (opc==2):
        mostrarPecado()

print("Adios")





