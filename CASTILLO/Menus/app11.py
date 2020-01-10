import libreria

def nuevoAlumno():
    # 1. Pedir nombre
    # 2. Pedir edad
    # 3. Guardadr datos en info.txt
    nombre=libreria.pedir_nombre("Ingrese nombre: ")
    edad=libreria.pedir_numero("Ingrese edad: " , 0, 100)
    contenido = nombre + "-" + str(edad) + "\n"
    libreria.guardar_datos("app11.txt", contenido,"a")
    print("Alumno nuevo guardado")

def mostrarAlumno():
    # 1. Acceder archivo info.txt
    # 2. Mostrar datos
    datos=libreria.obtener_datos_lista("app11.txt")
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

    opc= libreria.pedir_numero("Ingrese opcion: " , 1,3)
    if (opc==1):
        nuevoAlumno()

    if (opc==2):
        mostrarAlumno()

print("Adios")





