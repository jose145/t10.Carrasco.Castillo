import libreria2

def nuevoDia():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO DIA  ###########")
        print("# 1. Ingrese datos del dia       #")
        print("# 2. Mostrar datos del Dia       #")
        print("# 3. Salir                       #")
        print("##################################")

        opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
        if (opc==1):
            # 1. Pedir numero
            # 2. Pedir dia
            # 3. Guardadr datod en info.txt
            numero=libreria2.pedir_numero("Ingrese numero: " , 1 , 7)
            dia=libreria2.pedir_dia("Ingrese dia: " )
            contenido = str(numero) + "-" + str(dia) + "\n"
            libreria2.guardar_datos("app12.1.txt", contenido,"a")
            print("Dia nuevo guardado")

        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app12.1.txt")
            if ( datos != ""):
                    for item in datos:
                        numero, dia= item.split("-")
                        msg=" El numero del dia {} es {}"
                        numero=numero.replace("\n","")
                        dia=dia.replace("\n","")
                        print(msg.format(dia, str(numero)))

            else:
                print("Archivo vacio")


def mostrarDia():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app12.1.txt")
    if ( datos != ""):
        for item in datos:
            numero, dia= item.split("-")
            msg=" El numero de {} es {} "
            numero=numero.replace("\n","")
            dia=dia.replace("\n","")
            print(msg.format(dia, str(numero)))

    else:
        print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Dia              #")
    print("# 2. Mostrar Dia            #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoDia()

    if (opc==2):
        mostrarDia()

print("Adios")
