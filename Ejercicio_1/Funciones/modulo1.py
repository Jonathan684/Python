def promedio (cantidad_letras, cantidad_palabras):

    return cantidad_letras / cantidad_palabras

def cantidad_letras (cadena):
    cantidad = 0
    for i in cadena:
        cantidad += 1
    return cantidad

def buscar_re (cadena):
    hay_re = 0
    contiene_r = False
    print('llegó '+ cadena)
    for letra in cadena:  ## remedio     r e m e d
        if letra == 'r' :
            contiene_r = True
        if (letra == 'e') and (contiene_r == True):
            hay_re += 1
            contiene_r = False
    return hay_re


