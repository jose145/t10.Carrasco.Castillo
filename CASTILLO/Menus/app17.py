import libreria

def nuevoTalla():
    # 1. Pedir Talla
    # 2. Pedir Persona
    # 3. Guardadr datos en info.txt
    talla=libreria.pedir_talla("Ingrese Talla: ")
    persona=libreria.pedir_nombre("Ingrese Nombre: ")
    contenido = persona + "-" + str(talla) + "\n"
    libreria.guardar_datos("app17.txt", contenido,"a")
    print("Talla nuevo guardado")

def mostrarTalla():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app17.txt")
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

    opc= libreria.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoTalla()

    if (opc==2):
        mostrarTalla()

print("Adios")
