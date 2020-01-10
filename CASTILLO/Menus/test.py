import libreria

assert (libreria.validar_entero("hola") == False)
assert (libreria.validar_entero(15) == True)
assert (libreria.validar_entero("h") == False)
print( "Validar entero => ok ")

assert ( libreria.validar_rango(3,1,5) == True)
assert ( libreria.validar_rango("hola",1,5) == False)
assert ( libreria.validar_rango(32,11,50) == True)
print( "Validar rango => ok ")

assert (libreria.validar_nombre("nombre") == True)
assert (libreria.validar_nombre(4582) == False)
assert (libreria.validar_nombre("Luis") == True)
print( "Validar nombre => ok")

assert (libreria.validar_telefono("913927376") == False)
assert (libreria.validar_telefono(913927376) == True)
assert (libreria.validar_telefono(9139273) == False)
print( "Validar telf => ok")

assert (libreria.validar_dni(91392737) == True)
assert (libreria.validar_dni(913927376) == False)
assert (libreria.validar_dni("9139273") == False)
print( "Validar dni => ok")

assert (libreria.validar_nombre(20) == False)
assert (libreria.validar_nombre("LUIS") == True)
assert (libreria.validar_nombre("Juan") == True)
print( "Validar nombre => ok")

assert (libreria.validar_talla(20) == False)
assert (libreria.validar_talla("LUIS") == False)
assert (libreria.validar_talla(1.20) == True)
print( "Validar talla => ok")

assert (libreria.validar_codigo("1545-4") == False)
assert (libreria.validar_codigo("LUI-S") == False)
assert (libreria.validar_codigo("193679-A") == True)
print( "Validar codigo => ok")

assert (libreria.validar_estacion("azul") == False)
assert (libreria.validar_estacion("LUI-S") == False)
assert (libreria.validar_estacion("verano") == True)
print( "Validar estacion => ok")

assert (libreria.validar_pecado("azul") == False)
assert (libreria.validar_pecado("LUI-S") == False)
assert (libreria.validar_pecado("orgullo") == True)
print( "Validar pecado => ok")

assert (libreria.validar_dia("azul") == False)
assert (libreria.validar_dia("LUI-S") == False)
assert (libreria.validar_dia("LUNES") == True)
print( "Validar dia => ok")

assert (libreria.validar_peso(20) == False)
assert (libreria.validar_peso("LUIS") == False)
assert (libreria.validar_peso(31.20) == True)
print( "Validar peso => ok")
