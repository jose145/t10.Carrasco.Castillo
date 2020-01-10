import libreria2

def nuevoPeso():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO PESO  ###########")
        print("# 1. Ingrese datos del Nuevo Peso #")
        print("# 2. Mostrar datos del Nuevo Peso #")
        print("# 3. Salir                        #")
        print("###################################")

        opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
        if (opc==1):
            # 1. Pedir Peso
            # 2. Pedir Persona
            # 3. Guardadr datos en info.txt
            peso=libreria2.pedir_peso("Ingrese Peso: ")
            persona=libreria2.pedir_nombre("Ingrese Nombre: ")
            contenido = persona + "-" + str(peso) + "\n"
            libreria2.guardar_datos("app16.1.txt", contenido,"a")
            print("Peso nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app16.1.txt")
            if ( datos != ""):
                for item in datos:
                    persona, peso= item.split("-")
                    msg="La persona es {} y pesa {} Kg"
                    persona= persona.replace("\n","")
                    peso=peso.replace("\n","")
                    print(msg.format(persona, str(peso)))

            else:
                print("Archivo vacio")

def mostrarPeso():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app16.1.txt")
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

    opc= libreria2.pedir_numero("Ingrese opcion: ", 1 , 3)
    if (opc==1):
        nuevoPeso()

    if (opc==2):
        mostrarPeso()

print("Adios")
