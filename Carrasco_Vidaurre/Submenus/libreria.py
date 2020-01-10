#validar entero

def validar_entero(numero_positivo):
    if(isinstance(numero_positivo,int)==True and numero_positivo>=0 and
        isinstance(numero_positivo,bool)==False):
        return True

    else:
        return False
    #fin_def


def agregar_datos (ruta_archivo,contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()


def mostrar_datos (ruta_archivo):
    archivo=open(ruta_archivo, "r")
    datos=archivo.read()
    archivo.close()
    return datos

def validar_opcion(nro,r1,r2):
    if(nro<r1 or nro>r2):
        print("opcion invalida")


def validar_nombre(nombre):
    #Validar si es una cadena y no tenga forma de numero
    if(isinstance(nombre,str)==True and nombre.isdigit()==False):

        #verificar si el nombre tiene mas de 3 letras
        cadena=False
        if(len(nombre)>=3 ):
            cadena=True#->este es va como una prueba
        #fin if

        #verificar si en el nombre tiene un numero o una coma o un punto
        nombre_con_nro=False
        for i in nombre:
            if(i.isdigit()==True or i=="." or i=="," or i==";"):
                nombre_con_nro=True#->este es va como una prueba
            #fin de for

        #Si ya pasaron las pruebas anteriores ahora si puede retornar True o False
        if(cadena==True and nombre_con_nro==False):
            return True
        #fin if

        #si no pasan las pruebas retornara False
        else:
            return False
    #de lo contrario retornara False
    else:
        return False
#fin funcion


#Funcion de pedir nombre
def pedir_nombre():
    nombre=14#-> obligamos a  que entre en el bucle
    while(validar_nombre(nombre)==False):
        nombre=input("Ingrese nombre:")
    return (nombre+" ")
#fin funcion


#validar codigo universitario
# 0123456
# 193678E
def validar_codigo(codigo):
    if(len(codigo)==7):#->verificar si el codigo tenga una longitud de 7
        letra=codigo[6:]#->esta variable es para la pocicion de la ultima letra
        valido_letra=False#->la variable es para ver si esta correcto la leta

        #verificar si la ultima letra sea una letra del abecedario
        if(letra.upper()=="A" or letra.upper()=="B" or letra.upper()=="C" or letra.upper()=="D" or
        letra.upper()=="E" or letra.upper()=="F" or letra.upper()=="G" or letra.upper()=="H" or
        letra.upper()=="I" or letra.upper()=="J" or letra.upper()=="K" or letra.upper()=="L" or
        letra.upper()=="M" or letra.upper()=="N" or letra.upper()=="O" or letra.upper()=="P" or
        letra.upper()=="Q" or letra.upper()=="R" or letra.upper()=="S" or letra.upper()=="T" or
        letra.upper()=="U" or letra.upper()=="V" or letra.upper()=="W" or letra.upper()=="X" or
        letra.upper()=="Z" or letra.upper()=="Z"):
            valido_letra=True
        nro=codigo[0:6]
        valido_nro=False
        if (validar_entero(int(nro))==True and nro.isdigit()==True):
            valido_nro=True
        if (valido_letra==True and valido_nro==True):
            return True
        else:
            return False

    else:
        return False
#fin funcion


#pedir codigo
def pedir_codigo():
    codigo="12"
    while(validar_codigo(codigo)==False):
        codigo=input("Ingrese codigo:")
    return codigo
#fin funcion




# funcion para guardar los datos del alumno
def alumno_nacional():
    lista=[]
    nombre=pedir_nombre()
    print("nombre guardado")
    lista.append(nombre)
    codigo=pedir_codigo()
    print("codigo guardado")
    lista.append(codigo)


    agregar_datos("Submenu1.txt","","w")

    contenido=("-->Nacional\n"+"Nombre:"+str(lista[0])+"\n")
    agregar_datos("Submenu1.txt",contenido,"a")


    agregar_datos("Submenu1.txt","Codigo: "+str(lista[1])+"\n","a")



# funcion para guardar los datos del alumno
def alumno_particular():

    lista=[]
    nombre=pedir_nombre()
    print("nombre guardado")
    lista.append(nombre)
    codigo=pedir_codigo()
    print("codigo guardado")
    lista.append(codigo)

    if (mostrar_datos("Submenu1.txt")==""):
        contenido=("-->Particular\n"+"Nombre:"+str(lista[0])+"\n")
        agregar_datos("Submenu1.txt",contenido,"w")
        agregar_datos("Submenu1.txt","Codigo: "+str(lista[1])+"\n","a")

    else:
        contenido=("-->Particular\n"+"Nombre:"+str(lista[0])+"\n")
        agregar_datos("Submenu1.txt",contenido,"a")
        agregar_datos("Submenu1.txt","Codigo: "+str(lista[1])+"\n","a")
#fin funcion




#validar correo electronico de gmail
#el correo debe tener el "@gmail.com"
def validar_correo(correo_electronico):
    arroba=False
    for a in correo_electronico:#-> interamos para ver si esta el signo arroba en el correo
        if(a =="@"):
            arroba=True
    if(arroba==True):#->aca entra cuando se verifica que esta la arroba
        validar=correo_electronico.split("@")#-> separamos la cadena en el @
        for i in validar:#-> interamos para ver si tiene el gmail.com
            gmail=False#-> variable para ver si esta en el correro esta el gmail.com
            #validar si esta el gmail.com
            if (i =="gmail.com"):
                gmail=True
        if (gmail==True):# con la variable creada (gmail) veremos si es correcto el gmail
            return True
        else:
            return False
    else:#-> de lo contrario el correo sera invalido
        return False

#fin funcion


#pedir correo
def pedir_correo():
    correo="Hola"
    while(validar_correo(correo)==False):
        correo=input("Ingrese correo electronico:")
    return correo
#fin funcion



#validar telefono
def validar_telefono(nro):
    cad=str(nro)
    if(len(cad)==9 and isinstance(nro,int)==True and validar_entero(nro)==True):
        return True
    else:
        return False
#fin funcion


#pedir telefono
def pedir_telefono():
    nro=251
    while(validar_telefono(nro)==False):
        nro=int(input("Ingrese Nº de telefono:"))
    return nro
#fin funcion


#submenu 02
# funcion para guardar los datos del alumno
def alumno():
    lista=[]
    correo=pedir_correo()
    print("correo guardado")
    lista.append(correo)
    telefono=pedir_telefono()
    print("Numero de telefono guardado")
    lista.append(telefono)


    agregar_datos("Submenu2.txt","","w")

    contenido=("-->Alumno\n"+"Correo: "+str(lista[0])+"\n")
    agregar_datos("Submenu2.txt",contenido,"a")


    agregar_datos("Submenu2.txt","Nro De telefono: "+str(lista[1])+"\n","a")



def docente():

    lista=[]
    correo=pedir_correo()
    print("correo guardado")
    lista.append(correo)
    telefono=pedir_telefono()
    print("Nro de telefono guardado")
    lista.append(telefono)

    if (mostrar_datos("Submenu2.txt")==""):
        contenido=("-->Docente\n"+"Correo :"+str(lista[0])+"\n")
        agregar_datos("Submenu2.txt",contenido,"w")
        agregar_datos("Submenu2.txt","Nro telefono : "+str(lista[1])+"\n","a")

    else:
        contenido=("-->Docente\n"+"Correo:"+str(lista[0])+"\n")
        agregar_datos("Submenu2.txt",contenido,"a")
        agregar_datos("Submenu2.txt","Nro de telefono: "+str(lista[1])+"\n","a")
#fin funcion




#validar el rango de 1 hasta 3
def validar_fecha(fecha):
    anio=False
    mes=False
    dia=False
    gion=False
    if(len(fecha)==10):
        if(fecha[0:4].isdigit()==True):
            anio=True
        if(fecha[5:7].isdigit()==True and int(fecha[5:7])<=12 and int(fecha[5:7])>0 ):
            mes=True
        if(fecha[8::].isdigit()==True and int(fecha[8::])<=31 and int(fecha[8::])>0):
            dia=True
        if (fecha[4:5]=="-" and fecha[7:8]=="-"):
            gion=True
        if(anio==True and mes==True and dia==True and gion==True):
            return True
        else:
            return False
    else:
        return False
    #Fin funcion


#validar dni
def validar_dni(dni):
    cad=str(dni)
    if (len(cad)==8):
        if(validar_entero(dni)==True):
            return True
        else:
            return False

    else:
        return False
    #fin funcion


#validar edad
def validar_edad_menor(edad):
    if(validar_entero(edad)==True):
        if (edad<0 or edad >=18):
            return False
        else:
            return True
    else:
        return False
    #fin funcion


#pedir edad
def pedir_edad_menor ():
    edad=-14
    while(validar_edad_menor(edad)==False):
        edad=int(input("Ingrese edad:"))
    return edad
#fin funcion

#pedir dni
def pedir_dni():
    dni=1
    while(validar_dni(dni)==False):
        dni=int(input("Ingrese DNI:"))
    return dni


def validar_edad_mayor(edad):
    if(validar_entero(edad)==True):
        if (edad>=18 and edad<100):
            return True
        else:
            return False
    else:
        return False
    #fin funcion


#pedir edad
def pedir_edad_mayor():
    edad=-14
    while(validar_edad_mayor(edad)==False):
        edad=int(input("Ingrese edad:"))
    return edad
#fin funcion


#submenu 03
# funcion para guardar los datos del menor
def menor():
    lista=[]
    edad=pedir_edad_menor()
    print("edad guardado")
    lista.append(edad)
    dni=pedir_dni()
    print("DNI guardado")
    lista.append(dni)


    agregar_datos("Submenu3.txt","","w")

    contenido=("-->Menor de edad\n"+"Edad: "+str(lista[0])+"\n")
    agregar_datos("Submenu3.txt",contenido,"a")


    agregar_datos("Submenu3.txt","DNI : "+str(lista[1])+"\n","a")



def adulto():

    lista=[]
    edad=pedir_edad_mayor()
    print("edad guardado")
    lista.append(edad)
    dni=pedir_dni()
    print("DNI guardado")
    lista.append(dni)

    if (mostrar_datos("Submenu3.txt")==""):
        contenido=("-->Mayor de edad\n"+"Edad :"+str(lista[0])+"\n")
        agregar_datos("Submenu3.txt",contenido,"w")
        agregar_datos("Submenu3.txt","DNI : "+str(lista[1])+"\n","a")

    else:
        contenido=("-->Adulto\n"+"Edad :"+str(lista[0])+"\n")
        agregar_datos("Submenu3.txt",contenido,"a")
        agregar_datos("Submenu3.txt","DNI : "+str(lista[1])+"\n","a")
#fin funcion


#validar Facultad
def validar_facultad(facultad):
    if (facultad.title()=="Facultad De Agronomia" or facultad.title()=="Facultad De Ciencias Biologicas" or
    facultad.title()=="Facultad De Ciencias Economicas, Administrativas Y Contables" or facultad.title()=="Facultad De Ciencias Fisicas Y Matematicas"
    or facultad.title()=="Facultad De Ciencias Historico Sociales Y Educacion" or facultad.title()=="Facultad De Derecho Y Ciencias Politicas"
    or facultad.title()=="Facultad De Enfermeria" or facultad.title()=="Facultad De Ingenieria Agricola" or
    facultad.title()=="Facultad De Ingenieria Civil, De Sistemas Y De Arquitectura" or
    facultad.title()=="Facultad De Ingenieria Mecanica Electrica" or facultad.title()=="Facultad De Medicina Humana" or
    facultad.title()=="Facultad De Medicina Veterinaria" or facultad.title()=="Facultad De Ingenieria Quimica E Industrias Alimentarias" or
    facultad.title()=="Facultad De Zootecnia"):
        return True
    else:
        return False

def pedir_facultad():
    facultad="Hola"
    while(validar_facultad(facultad)==False):
        facultad=input("Ingrese facultad:")
    return facultad


#submenu 04
def estudiante():
    lista=[]
    nombre=pedir_nombre()
    print("Nombre guardado")
    lista.append(nombre)
    facultad=pedir_facultad()
    print("Facultad guardado")
    lista.append(facultad)


    agregar_datos("Submenu4.txt","","w")

    contenido=("-->Estudiante\n"+"nombre: "+str(lista[0])+"\n")
    agregar_datos("Submenu4.txt",contenido,"a")


    agregar_datos("Submenu4.txt","Facultad : "+str(lista[1])+"\n","a")
#fin funcion



#validar meses
def validar_nro_meses(meses):
    #validar si es nombrado o contratado
    if(validar_entero(meses)==True):
        if (meses>0 and meses<=12):
            return True
        else:
            return False
    else:
        return False
#fin funcion


#pedir mese de trabajo
def pedir_mes():
    mes=-1
    while(validar_nro_meses(mes)==False):
        mes=int(input("Meses de Trabajo:"))
    return mes


#submenu 05
# funcion para guardar los datos del contratado
#contratado-->1 mes =5000soles
#nombrado-->1mes =10000soles
def contratado():
    lista=[]
    nombre=pedir_nombre()
    print("nombre guardado")
    lista.append(nombre)
    mes=(pedir_mes()*5000)
    print("dato guardado")
    lista.append(mes)


    agregar_datos("Submenu5.txt","","w")

    contenido=("-->Contratado\n"+"Nombre: "+str(lista[0])+"\n")
    agregar_datos("Submenu5.txt",contenido,"a")


    agregar_datos("Submenu5.txt","Sueldo : "+str(lista[1])+"\n","a")



def nombrado():

    lista=[]
    nombre=pedir_nombre()
    print("nombre guardado")
    lista.append(nombre)
    mes=pedir_mes()*10000
    print("dato guardado")
    lista.append(mes)

    if (mostrar_datos("Submenu5.txt")==""):
        contenido=("-->Nombrado\n"+"Nombre:"+str(lista[0])+"\n")
        agregar_datos("Submenu5.txt",contenido,"w")
        agregar_datos("Submenu5.txt","Sueldo : "+str(lista[1])+"\n","a")

    else:
        contenido=("-->Nombrado\n"+"Nombre :"+str(lista[0])+"\n")
        agregar_datos("Submenu5.txt",contenido,"a")
        agregar_datos("Submenu5.txt","Sueldo : "+str(lista[1])+"\n","a")
#fin funcion


#validar un numero entero
def validar_nro(nro):
    if(isinstance(nro,bool)==False):
        if(isinstance(nro,int)==True or isinstance(nro,float)==True ):
            return True
        else:
            return False
    else:
        return False
#fin funcion


#pedir nro
def pedir_nro():
    nro="HOla"
    while(validar_nro(nro)==False):
        nro=float(input("Ingrese numero:"))
    return nro


#submenu 06
# funcion para guardar los datos de la operacion multiplicar y dividir
def multiplicar():
    lista=[]
    nro01=pedir_nro()
    print("1er numero guardado")
    lista.append(nro01)
    nro02=pedir_nro()
    print("2do numero guardado")
    lista.append(nro02)


    agregar_datos("Submenu6.txt","","w")

    contenido=("-->Multiplicar\n"+"1er numero: "+str(lista[0])+"\n")
    agregar_datos("Submenu6.txt",contenido,"a")


    agregar_datos("Submenu6.txt","2do numero: "+str(lista[1])+"\n","a")
    total=nro01*nro02
    agregar_datos("Submenu6.txt","Total: "+str(total)+"\n","a")



def dividir():

    lista=[]
    nro01=pedir_nro()
    print("1er numero guardado")
    lista.append(nro01)
    nro02=pedir_nro()
    print("2do numero guardado")
    lista.append(nro02)

    if (mostrar_datos("Submenu6.txt")==""):
        contenido=("-->Dividir\n"+"1er numero:"+str(lista[0])+"\n")
        agregar_datos("Submenu6.txt",contenido,"w")
        agregar_datos("Submenu6.txt","2do numero: "+str(lista[1])+"\n","a")
        total=nro01/nro02
        agregar_datos("Submenu6.txt","Total: "+str(total)+"\n","a")


    else:
        contenido=("-->Dividir \n"+"1er numero:"+str(lista[0])+"\n")
        agregar_datos("Submenu6.txt",contenido,"a")
        agregar_datos("Submenu6.txt","2do numero : "+str(lista[1])+"\n","a")
        total=nro01/nro02
        agregar_datos("Submenu6.txt","Total: "+str(total)+"\n","a")
#fin funcion



#submenu 07
# funcion para guardar los datos de la operacion sumar y restar
def sumar():
    lista=[]
    nro01=pedir_nro()
    print("1er numero guardado")
    lista.append(nro01)
    nro02=pedir_nro()
    print("2do numero guardado")
    lista.append(nro02)


    agregar_datos("Submenu7.txt","","w")

    contenido=("-->Sumar\n"+"1er numero: "+str(lista[0])+"\n")
    agregar_datos("Submenu7.txt",contenido,"a")


    agregar_datos("Submenu7.txt","2do numero: "+str(lista[1])+"\n","a")
    total=nro01+nro02
    agregar_datos("Submenu7.txt","Total: "+str(total)+"\n","a")



def restar():

    lista=[]
    nro01=pedir_nro()
    print("1er numero guardado")
    lista.append(nro01)
    nro02=pedir_nro()
    print("2do numero guardado")
    lista.append(nro02)

    if (mostrar_datos("Submenu7.txt")==""):
        contenido=("-->Restar\n"+"1er numero:"+str(lista[0])+"\n")
        agregar_datos("Submenu7.txt",contenido,"w")
        agregar_datos("Submenu7.txt","2do numero: "+str(lista[1])+"\n","a")
        total=nro01-nro02
        agregar_datos("Submenu7.txt","Total: "+str(total)+"\n","a")


    else:
        contenido=("-->Restar\n"+"1er numero:"+str(lista[0])+"\n")
        agregar_datos("Submenu7.txt",contenido,"a")
        agregar_datos("Submenu7.txt","2do numero : "+str(lista[1])+"\n","a")
        total=nro01-nro02
        agregar_datos("Submenu7.txt","Total: "+str(total)+"\n","a")
#fin funcion




#validar tipo de colegio(Nacional,PArticular)
def validar_tipo_colegio(colegio):
    if (colegio.upper()=="NACIONAL" or colegio.upper()=="PARTICULAR"):
        return True
    else:
        return False

#pedir tipo de colegio
def pedir_colegio():
    colegio="Hola"
    while(validar_tipo_colegio(colegio)==False):
        colegio=input("Ingrese tipo de colegio(Nacional,Particular):")
    return colegio


#submenu 08
def postulante():
    lista=[]
    nombre=pedir_nombre()
    print("Nombre guardado")
    lista.append(nombre)
    colegio=pedir_colegio()
    print("dato guardado")
    lista.append(colegio)


    agregar_datos("Submenu8.txt","","w")

    contenido=("-->Postulante\n"+"nombre: "+str(lista[0])+"\n")
    agregar_datos("Submenu8.txt",contenido,"a")

    agregar_datos("Submenu8.txt","Tipo de colegio : "+str(lista[1])+"\n","a")

    if (colegio.upper()=="NACIONAL"):
        agregar_datos("Submenu8.txt","Costo del examen : "+str(280)+"\n","a")
    if (colegio.upper()=="PARTICULAR"):
        agregar_datos("Submenu8.txt","Costo del examen : "+str(380)+"\n","a")
#fin funcion
