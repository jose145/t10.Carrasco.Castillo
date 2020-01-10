import libreria

def nuevoTelf():
    # 1. Pedir Telefono
    # 2. Pedir Empresa
    # 3. Guardadr datos en info.txt
    Telefono=libreria.pedir_telf("Ingrese numero de telefono: ")
    Usuario=libreria.pedir_nombre("Ingrese nombre de usuario: ")
    contenido = Usuario + "-" + str(Telefono) + "\n"
    libreria.guardar_datos("app13.txt", contenido,"a")
    print("Telefono nuevo guardado")

def mostrarTelf():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app13.txt")
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
    opc= libreria.pedir_numero("Ingrese opcion: ",1,3)

    if (opc==1):
        nuevoTelf()

    if (opc==2):
        mostrarTelf()

print("Adios")
