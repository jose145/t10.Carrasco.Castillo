import libreria2

def nuevoAlumno():
    opc=0
    max=3
    while ( opc != max ):
        print("########### NUEVO ALUMNO  ###########")
        print("# 1. Ingrese datos del alumno       #")
        print("# 2. Mostrar datos del alumno       #")
        print("# 3. Salir                          #")
        print("#####################################")

        opc= libreria2.pedir_numero("Ingrese opcion: ", 1, 3)
        if (opc==1):
            # 1. Pedir nombre
            # 2. Pedir edad
            # 3. Guardadr datos en info.txt
            nombre=libreria2.pedir_nombre("Ingrese nombre: ")
            edad=libreria2.pedir_numero("Ingrese edad: ", 0, 100)
            contenido = nombre + "-" + str(edad) + "\n"
            libreria2.guardar_datos("app11.1.txt", contenido, "a")
            print("Alumno nuevo guardado")


        if (opc==2):
            # 1. Acceder archivo info.txt
            # 2. Mostrar datos
            datos=libreria2.obtener_datos_lista("app11.1.txt")
            if ( datos != ""):
                    for item in datos:
                        nombre, edad= item.split("-")
                        msg=" El alumno es {} y tiene {} anios"
                        nombre=nombre.replace("\n","")
                        edad=edad.replace("\n","")
                        print(msg.format(nombre, str(edad)))

            else:
                print("Archivo vacio")

def mostrarAlumno():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria2.obtener_datos_lista("app11.1.txt")
    if ( datos != ""):
         for item in datos:
            nombre, edad= item.split("-")
            msg=" El alumno es {} y tiene {} anios"
            nombre=nombre.replace("\n","")
            edad=edad.replace("\n","")
            print(msg.format(nombre, str(edad)))

    else:
         print("Archivo vacio")

opc=0
max=3
while ( opc != max ):
    print("########### MENU  ###########")
    print("# 1. Nuevo Alumno           #")
    print("# 2. Mostrar Alumnos        #")
    print("# 3. Salir                  #")
    print("#############################")

    opc= libreria2.pedir_numero("Ingrese opcion: ", 1, 3)
    if (opc==1):
        nuevoAlumno()

    if (opc==2):
        mostrarAlumno()

print("Adios")





