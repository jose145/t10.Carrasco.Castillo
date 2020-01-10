#programa que pide nro de DNI y el genero de la persona
import libreria

max=4
opc=0
while(opc!=max):
    #mostrar menu de opciones
    print("1: Ingrese Nº de DNI")
    print("2: Sexo(M\F)")
    print("3: Mostar datos")
    print("4: Salir")
    opc=int(input("Ingrese opcion:"))
    validar_opcion=libreria.validar_opcion(opc,1,3)
    #si se ingresa la opc 1 pedira el Nº de DNI

    lista=[]

    if(opc==1):
        dni=libreria.pedir_dni()
        lista.append(dni)
        #fin if
    #si se ingresa la opc 2 pedira el Sexo
    if(opc==2):
        sexo=(libreria.pedir_sexo())
        lista.append(sexo)
        #fin if
    for i in lista:
        if (isinstance(i,int)==True):
            libreria.agregar_datos("Menu3.txt","DNI: "+str(i)+" - ","w")
        if (isinstance(i,str)==True):
            libreria.agregar_datos("Menu3.txt","Sexo: "+i,"a")
    #si se ingresa 3 entonces mostrara datos
    if(opc==3):
        mostar=libreria.mostrar_datos("Menu3.txt")
        print("--->"+mostar)


