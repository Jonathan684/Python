def read():
    return


def validar(min, max, cadena):
    # n = input('Ingrese cantidad de datos: ')
    while True:  # Mientras tal cosa (True)
        n = int(input(cadena))
        if (n > min) and (n < max):
            return n
        else:
            print('ERROR! Ingrese un valor correcto: ')


def cargar_datos(cantidad_de_datos):
    ##n = int(input("Ingrese la cantidad de muestras a registrar: "))
    temperaturas = [0] * cantidad_de_datos
    regiones = [0] * cantidad_de_datos
    días = [0] * cantidad_de_datos
    for i in range(cantidad_de_datos):  ## 0 1 2 3 4
        día = validar(0, 31, 'Ingrese el día del mes en el que se registró la temperatura:')
        # día = int(input('Ingrese el día del mes en el que se registró la temperatura:'))
        temperatura = float(input('Ingrese temperatura registrada: '))
        región = validar(1, 20, 'Ingrese región del 1 al 20: ')
        días[i] = día
        regiones[i] = región
        temperaturas[i] = temperatura
        print('_' * 80)
        print('SIGUIENTE')
    return días, regiones, temperaturas


def principal():
    print('Inicio del programa')
    num = 0
    cantidad_de_datos = validar(num, 99999, 'Ingrese cantidad de datos: ')
    print(cantidad_de_datos)
    Temperaturas = cantidad_de_datos * [0]
    días = cantidad_de_datos * [0]
    regiones = cantidad_de_datos * [0]
    días, regiones, Temperaturas = cargar_datos(cantidad_de_datos)
    print(días)
    print(regiones)
    print(Temperaturas)


if '_name_== _main_':
    principal()
# step
# validate()
# n > 0
# False = 0
# True = 1
