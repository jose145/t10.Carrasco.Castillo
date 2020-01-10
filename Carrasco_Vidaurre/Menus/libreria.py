def agregar_datos (ruta_archivo,contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()


def mostrar_datos (ruta_archivo):
    archivo=open(ruta_archivo, "r")
    datos=archivo.read()
    archivo.close()
    return datos


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


#pedir fecha
def pedir_fecha():
    fecha="0"
    while(validar_fecha(fecha)==False):
        fecha=input("Ingrese fecha(AÑO-MES-DIA):")
    return (fecha+" ")
#fin funcion



#validar entero

def validar_entero(numero_positivo):
    if(isinstance(numero_positivo,int)==True and numero_positivo>=0 and
        isinstance(numero_positivo,bool)==False):
        return True

    else:
        return False
    #fin_def

#Validar DNI

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


#Validar sexo
def validar_sexo(sexo):
    if(isinstance(sexo,str)==True):
        cad=sexo.upper()
        if(cad=="FEMENINO" or cad=="MASCULINO"):
            return True
        else:
            return False
    else:
        return False
    #fin funcion


#pedir dni
def pedir_dni():
    dni=1
    while(validar_dni(dni)==False):
        dni=int(input("Ingrese DNI:"))
    return dni

#pedir sexo
def pedir_sexo():
    sexo=0
    while(validar_sexo(sexo)==False):
        sexo=input("Ingrese Sexo(Masculino\Femenino):")
    return sexo.upper()



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


#validar edad
def validar_edad(edad):
    if(validar_entero(edad)==True):
        if (edad<0 or edad >100):
            return False
        else:
            return True
    else:
        return False
    #fin funcion



#pedir edad
def pedir_edad ():
    edad=-14
    while(validar_edad(edad)==False):
        edad=int(input("Ingrese edad:"))
    return edad
#fin funcion



#validar mes
def validar_mes(mes):
    if(mes.upper()=="ENERO" or mes.upper()=="FEBRERO" or mes.upper()=="MARZO" or
    mes.upper()=="ABRIL" or mes.upper()=="MAYO" or mes.upper()=="JUNIO" or
    mes.upper()=="JULIO" or mes.upper()=="AGOSTO" or mes.upper()=="SEPTIEMBRE" or
    mes.upper()=="OCTUBRE" or mes.upper()=="NOVIEMBRE" or mes.upper()=="DICIEMBRE"):
        return True
    else:
        return False
#fin funcion




#pedir mes
def pedir_mes():
    mes="hola"
    while(validar_mes(mes)==False):
        mes=input("Ingrese mes:")
    return mes
#fin funcion



#validar nro de asiento de un bus de 50
def validar_asiento(asiento):
    if(validar_entero(asiento)==True):
        if (asiento<1 or asiento>50):
            return False
        else:
            return True
    else:
        return False
#fin funcion

#pedir asiento
def pedir_asiento():
    asiento=-1
    while(validar_asiento(asiento)==False):
        asiento=int(input("Ingrese Nº de asiento:"))
    return asiento
#fin funcion





#Facultad de agronomia<
#Facultad de Ciencias Biologicas<
#Facultad de Ciencias Economicas, Administrativas ucontables<
#Facultad de Ciencias Fisicas y Matematicas<
#Facultad de Ciencias Historico Sociales y Educacion<
#Facultad de Derecho y ciencias politicas<
#Facultad de Enfermeria<
#Facultad de Ingenieria Agricola<
#Facultad de Ingenieria Civil, de sistemas y de arquitectura<
#Facultad de Ingenieria Mecanica electrica<
#Facultad de Medicina Humana<
#Facultad de Medicina Veterinaria<
#Facultad de Ingenieria quimica e industrias alimentarias
#Facultad de Zootecnia

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
