import libreria
assert (libreria.validar_entero("hola")==False)
assert (libreria.validar_entero(0.25)==False)
assert (libreria.validar_entero(True)==False)
assert (libreria.validar_entero("hola14")==False)
assert (libreria.validar_entero(-25)==False)



assert (libreria.validar_nombre("David11")==False)
assert (libreria.validar_nombre("20.5")==False)
assert (libreria.validar_nombre("Da12.5vid")==False)
assert (libreria.validar_nombre("David0.2")==False)
assert (libreria.validar_nombre("Da,vid")==False)
assert (libreria.validar_nombre("1David")==False)
assert (libreria.validar_nombre("david")==True)




assert (libreria.validar_codigo("14525A")==False)
assert (libreria.validar_codigo("Hla")==False)
assert (libreria.validar_codigo("-19367D")==False)
assert (libreria.validar_codigo("193678e")==True)
assert (libreria.validar_codigo("193678E")==True)


assert (libreria.validar_correo("davidjsmellgmail.com")==False)
assert (libreria.validar_correo("hola@")==False)
assert (libreria.validar_correo("hol")==False)
assert (libreria.validar_correo("dav@gma.com")==False)

assert (libreria.validar_telefono(-93590393)==False)
assert (libreria.validar_telefono("hola")==False)
assert (libreria.validar_telefono(True)==False)
assert (libreria.validar_telefono(0.1457891)==False)
assert (libreria.validar_telefono(935903932)==True)

assert(libreria.validar_fecha("2020-01-35")==False)
assert(libreria.validar_fecha("202-21-45")==False)
assert(libreria.validar_fecha("Hola-21-12")==False)


assert (libreria.validar_dni("hola")==False)
assert (libreria.validar_dni(1452544)==False)
assert (libreria.validar_dni(0.64)==False)
assert (libreria.validar_dni(-7653318)==False)
assert (libreria.validar_dni(76533186)==True)

assert (libreria.validar_edad_menor(200)==False)
assert (libreria.validar_edad_menor(-2)==False)
assert (libreria.validar_edad_menor("jola")==False)
assert (libreria.validar_edad_menor(0.25)==False)
assert (libreria.validar_edad_menor(14)==True)


assert (libreria.validar_edad_mayor(10)==False)
assert (libreria.validar_edad_mayor(-2)==False)
assert (libreria.validar_edad_mayor("jola")==False)
assert (libreria.validar_edad_mayor(0.25)==False)
assert (libreria.validar_edad_mayor(25)==True)

assert(libreria.validar_facultad("Facultad de agronomia")==True)
assert(libreria.validar_facultad("Facultad de Ciencias Biologicas")==True)
assert(libreria.validar_facultad("Facultad de Ciencias Economicas, Administrativas y contables")==True)
assert(libreria.validar_facultad("Facultad de Ciencias Fisicas y Matematicas")==True)
assert(libreria.validar_facultad("Facultad de Ciencias Historico Sociales y Educacion")==True)
assert(libreria.validar_facultad("Facultad de Derecho y ciencias politicas")==True)
assert(libreria.validar_facultad("Facultad de Ingenieria Agricola")==True)
assert(libreria.validar_facultad("Facultad de Ingenieria Civil, de sistemas y de arquitectura")==True)
assert(libreria.validar_facultad("Facultad de Ingenieria Mecanica electrica")==True)
assert(libreria.validar_facultad("Facultad de Medicina Humana")==True)
assert(libreria.validar_facultad("Facultad de Medicina veterinaria")==True)
assert(libreria.validar_facultad("Facultad de Ingenieria quimica e industrias alimentarias")==True)
assert(libreria.validar_facultad("Facultad de Zootecnia")==True)
assert(libreria.validar_facultad("Facultad de enfermeria")==True)



assert(libreria.validar_nro_meses(12)==True)
assert(libreria.validar_nro_meses(0)==False)
assert(libreria.validar_nro_meses(13)==False)
assert(libreria.validar_nro_meses(-2)==False)
assert(libreria.validar_nro_meses(1)==True)
assert(libreria.validar_nro_meses(5)==True)



assert(libreria.validar_nro(5)==True)
assert(libreria.validar_nro(-5)==True)
assert(libreria.validar_nro(0.36)==True)
assert(libreria.validar_nro("HOla")==False)
assert(libreria.validar_nro(True)==False)
assert(libreria.validar_nro(False)==False)



assert(libreria.validar_tipo_colegio("Nacional")==True)
assert(libreria.validar_tipo_colegio("Particular")==True)
assert(libreria.validar_tipo_colegio("nrijnds")==False)
assert(libreria.validar_tipo_colegio("nacional")==True)
assert(libreria.validar_tipo_colegio("particular")==True)

print ("Validado")
