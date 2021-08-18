import Funciones.modulo1 as fun
import Funciones.ventana as vent
vent.ventana()
#cadena = "Ahora estamos en octavos de final del mundial."
cadena = "El registro de goles ha revelado que el réferi se equivoca."
longitud_palabra = 0
contador = 0
palabra = ''
contador_de_letras = 0
contador_palabras_letrasmayor4 = 0
contador_comienza_con_t = 0
contador_de_re = 0
comienza_con_t = False
contiene_n = False
suma_letras = 0
suma_letras_2 = 0
contiene_a = False
contiene_s = False
no_contiene_e = True
contador_pasne = 0
promedio = 0

for letra in cadena:

    if letra == ' ' or letra == '.':  ## if true

        if contador_de_letras > 4 and contiene_n == True:
            contador_palabras_letrasmayor4 += 1
            contiene_n = False

        if comienza_con_t == True:
            contador_comienza_con_t += 1
            comienza_con_t = False
            suma_letras = suma_letras + fun.cantidad_letras(palabra)
            suma_letras_2 = suma_letras_2 + contador_de_letras

        if (contiene_a == True) and (contiene_s == True) and (no_contiene_e == True):
            contador_pasne += 1
            print('-->'+palabra)
    ## palabra[len(palabra)-1] obtenemos la ultima letra
        if palabra[len(palabra)-1] == 'o':
            contador_de_re += fun.buscar_re(palabra) ##cuanto re contiene

        palabra = '' ##limpiamos la palabra para volver a empezar
        contador += 1
        contiene_n = False
        contiene_s = False
        no_contiene_e = True
        contador_de_letras = 0

    else:
        contador_de_letras += 1 ## Cuenta las letras
        if(letra == 'n'):
            contiene_n = True
        palabra = palabra + letra
        if(palabra[0] == 't'):
            comienza_con_t = True
        ##print(palabra)
        if letra == 'a':
            contiene_a = True
        if letra == 's':
            contiene_s = True
        if letra == 'e': ## Analizar lo que tiene cuando analizamos lo que no tiene
            no_contiene_e = False ##  estamos es falso que no contiene e tiene e

if(contador_comienza_con_t != 0):
    promedio = fun.promedio(suma_letras, contador_comienza_con_t)


print("El promedio de palabras que comienzan con T", round(promedio))
print("Palabras mayor a 4 y que contiene n :",contador_palabras_letrasmayor4)
print("Las palbras que comienzan con T: ", contador_comienza_con_t)
print("Las palabras con T: ", suma_letras, suma_letras_2)
print('Las palabras que contienen "a", "s" y no "e", son: ', contador_pasne)
print('Palabras con "re" y finalizan con "o":' ,contador_de_re)