def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista

def validar_telefono(telf):
    if (isinstance(telf,int)):
        if(len(str(telf)) == 9):
            if(telf > 0):
                return True
            else:
                return False

        else:
            return False

    else:
        return False

def pedir_telf(nota):
    telf = 1457889989989
    while (validar_telefono(telf) == False):
        telf = int(input(nota))
    return telf

def validar_dni(dni):
    if (isinstance(dni,int)):
        if (len(str(dni)) == 8):
            return True
        else:
            return False
    else:
        return False

def pedir_DNI(nota):
    DNI = ""
    while (validar_dni(DNI) == False):
        DNI = int(input(nota))
    return DNI

def validar_real(real):
    if (isinstance(real,float)):
        return True
    else:
        return False

def pedir_real(nota):
    r = 2
    while (validar_real(r) == False):
        r = float(input(nota))
    return r

def validar_ruc(ruc):
    if (isinstance(ruc,int)):
        if (len(str(ruc)) == 11):
            return True
        else:
            return False
    else:
        return False

def pedir_ruc(nota):
    ruc = 0
    while (validar_ruc(ruc) == False):
        ruc = int(input(nota))
    return ruc

def validar_talla(talla):
    if (isinstance(talla,float)):
        if( talla >= 1.10 and talla <= 2.50):
            return True
        else:
            return False
    else:
        return False

def pedir_talla(nota):
    t = ""
    while (validar_talla(t) == False):
        t = float(input(nota))
    return t

def validar_codigo(codigo):
    # 1. Revisar que el nro de octetos sea 4
    data=codigo.split(".")
    if ( len(data) != 2):
        return False

    cod1 = data[0]
    cod2 = data[1]
    if ( cod1.isdigit() == False or cod2.isdigit() == True):
        return False

    # 4. Si llego hasta aqui, es porque es un IP valido
    return True

def pedir_codigo(nota):
    codigo_invalido=True
    while( codigo_invalido == True ):
        codigo=input(nota)
        codigo_invalido = ( validar_codigo(codigo) == False)
    #fin_while
    return codigo

def validar_estacion(estacion):
    if (estacion == "VERANO" or estacion == "INVIERNO" or
        estacion == "PRIMAVERA" or estacion == "OTONO" or
        estacion == "verano" or estacion == "invierno" or
        estacion == "primavera" or estacion == "otono" ):
        return True
    else:
        return False

def pedir_estacion(msg):
    estacion=""
    while ( validar_estacion(estacion) == False ):
        estacion=input(msg)
    #fin_while
    return estacion

def validar_pecado(pecado):
    if (pecado == "IRA" or pecado== "ENVIDIA" or
        pecado == "PEREZA" or pecado== "AVARICIA" or
        pecado == "LUJURIA" or pecado == "GULA" or
        pecado == "ORGULLO" or pecado == "ira" or
        pecado == "envidia" or pecado== "pereza" or
        pecado == "avaricia" or pecado== "lujuria" or
        pecado == "gula" or pecado == "orgullo" ):
        return True
    else:
        return False

def pedir_pecado(msg):
    pecado=""
    while ( validar_pecado(pecado) == False ):
        pecado=input(msg)
    #fin_while
    return pecado


def validar_dia(dia):
    if (dia == "LUNES" or dia== "MARTES" or
        dia == "MIERCOLES" or dia == "JUEVES" or
        dia == "VIERNES" or dia == "SABADO" or
        dia == "DOMINGO" or dia == "lunes" or
        dia == "martes" or dia == "miercoles" or
        dia == "jueves" or dia == "viernes" or
        dia == "sabado" or dia == "domingo" ):
        return True
    else:
        return False

def pedir_dia(msg):
    dia=""
    while ( validar_dia(dia) == False ):
        dia=input(msg)
    #fin_while
    return dia

def validar_peso(peso):
    if (isinstance(peso,float)):
        if( peso >= 20.0 and peso <= 100.0):
            return True
        else:
            return False
    else:
        return False

def pedir_peso(nota):
    p = ""
    while (validar_peso(p) == False):
        p = float(input(nota))
    return p
