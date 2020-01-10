import libreria

def nuevoPeso():
    # 1. Pedir Peso
    # 2. Pedir Persona
    # 3. Guardadr datos en info.txt
    peso=libreria.pedir_peso("Ingrese Peso: ")
    persona=libreria.pedir_nombre("Ingrese Nombre: ")
    contenido = persona + "-" + str(peso) + "\n"
    libreria.guardar_datos("app16.txt", contenido,"a")
    print("Peso nuevo guardado")

def mostrarPeso():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app16.txt")
    if ( datos != ""):
        for item in datos:
            persona, peso= item.split("-")
            msg="La persona es {} y pesa {} Kg"
            persona= persona.replace("\n","")
            peso=peso.replace("\n","")
            print(msg.format(persona, str(peso)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Peso             #")
    print("# 2. Mostrar Peso           #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoPeso()

    if (opc==2):
        mostrarPeso()

print("Adios")
