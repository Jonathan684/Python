__author__ = 'Nadia y Jonathan'
def es_digitos(num):
    if num in '0123456789':
        return True
    else:
        return False

def es_vocal(cadena):
    if cadena in 'AEIOUaeiou':
        return True
    else:
        return False

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def calcular_porcentaje(total, cantidad):
    if total != 0:
        porcentaje = (cantidad * 100) / total
        return porcentaje
    else:
        return 0

def es_consonante(cadena):
    if cadena in 'AEIOUaeiou':
        return False
    else:
        return True

def buscar_ma(cadena):
    hay_ma = 0
    contiene_m = False
    for letra in cadena:
        if letra == 'm':
            contiene_r = True
        if (letra == 'a') and (contiene_m == True):
            hay_ma += 1
            contiene_m = False
    return hay_ma


def principal():
    # adentro de la palabra
    cont_caracteres = 0
    cont_letras_totales = 0
    cont_palabras = 0
    cont_digitos = 0
    palabras_digitos_vocales = 0
    cont_vocales_por_palabra = 0
    cont_consonantes = 0
    cont_palabras_consonantes = 0
    palabras_con_consonantes = 0
    comienza_con_consonante = False
    termina_con_vocal = False
    palabras_empiezan_consonante_termina_vocal = 0
    palabras_con_ma = 0
    contador_de_ma = 0
    pal = ''
    anterior = ''
    ##cadena = input('Ingrese letra: ')
    cadena = "Mañanama forma."

    ##cadena = "Los códigos X12AEB y YAA123 de productos están en falta."
    for letra in cadena:

        ##CARACTERES h
        if (letra != ' ') and (letra != '.'):  ## Logica positiva o logica negativa No se tienen que cumplir los dos
            # ¿(no es ' ' )y (no es '.') ? = True
            cont_caracteres += 1
            cont_letras_totales += 1
            pal = pal + letra  ## Formando la palabra
            if (anterior in 'mM') and (letra == 'a'):

                contador_de_ma += 1

            anterior = letra
            ##print("-->"+letra+"<--")
            ##print(pal)
            if es_digitos(letra):
                cont_digitos += 1  # -> cantidad de digitos
            if es_vocal(letra):
                cont_vocales_por_palabra += 1
            if es_consonante(letra):
                cont_consonantes += 1
            if cont_caracteres == 1 and es_consonante(letra) == True:
                comienza_con_consonante = True

        # Afuera de la palabra
        ## PALABRA
        else:

            print('palabra :' + pal, "-->", buscar_ma(pal))
            if (cont_digitos >= 2) and (es_par(cont_vocales_por_palabra)):
                palabras_digitos_vocales += 1
            if cont_consonantes >= 3 and cont_digitos >= 1:
                palabras_con_consonantes += 1
            if es_vocal(anterior):
                termina_con_vocal = True
            if comienza_con_consonante and termina_con_vocal == True:
                print(pal)
                palabras_empiezan_consonante_termina_vocal += 1
            if contador_de_ma != 0 and es_par(contador_de_ma):
                palabras_con_ma += 1
            #print("Contador de ma", contador_de_ma)

            # if es_par(buscar_ma(pal)) == True:
            #   palabras_con_ma += 1

            ##reiniciar contadores
            pal = ''
            cont_digitos = 0
            cont_vocales_por_palabra = 0
            cont_palabras += 1
            cont_caracteres = 0
            termina_con_vocal = False
            comienza_con_consonante = False
            contador_de_ma = 0

    print('RESULTADOS')
    print('Las palabras con dos o más dígitos y una cantidad par de vocales son: ', palabras_digitos_vocales)

    porcentaje = calcular_porcentaje(cont_palabras, palabras_con_consonantes)

    print('El porcentaje de las palabras que tienen más de tres consonates:', porcentaje, '%')
    print('Las palabras que comienzan con consonante y termina con vocal son: ',
          palabras_empiezan_consonante_termina_vocal)
    print('Las palabras que tienen "MA" son: ', palabras_con_ma)


if __name__ == '__main__':
    principal()
