import os
import pickle
from registros import *
import random

'''
Una empresa proveedora de servicios de TV e Internet solicita un programa para gestionar su facturación. 
Por cada cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive),
tipo de producto (un valor en 0 y 15 inclusive), monto facturación mensual. A través de un menú de opciones, realizar los siguientes puntos:
1 - Cargar un vector de n facturas, validando todos los posibles valores,
   la carga puede ser manual, automática, o bien puede implementar ambas. 
   El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado por numero de identificación
2 - Mostar el contenido del vector a razón de un registro por línea
3 - Buscar una factura con numero de identificación X,
   donde X se carga por teclado. Si existe mostrar sus datos, caso contrario indicar con un mensaje
4 - A partir del arreglo del punto 1, generar una matriz por tipo de cliente y tipo de producto,
    donde cada componente contenga la cantidad de clientes  (144 contadores).
    Muestre de dicha matriz solo los valores que sean mayor a cero
5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo X ingresado por parámetro y
   que su tipo de producto no sean ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total facturado para todos esas facturas
6 - A partir del arreglo, para un tipo de producto X que se ingresa por teclado, informar cual fue el total facturado
    y que porcentaje representa sobre el total de facturas del arreglo.
'''

'''
    1 - Cargar un vector de n facturas, validando todos los posibles valores,
   la carga puede ser manual, automática, o bien puede implementar ambas. 
   El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado por numero de identificación
'''


def add_in_order(facturas, registro):
    izq, der = 0, len(facturas) - 1
    while izq <= der:
        c = (izq + der) // 2
        if facturas[c].num_id == registro.num_id:
            pos = c
            break
        if registro.num_id < facturas[c].num_id:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    facturas[pos:pos] = [registro]


def carga_automatica(facturas, n):
    nombre_titular = ['Jonathan', 'Candela', 'Nadia', 'Matías']
    for i in range(n):
        num_id = i
        nomb_titular = random.choice(nombre_titular)
        tipo_cliente = random.randint(0, 8)
        tipo_producto = random.randint(0, 15)  ## NO OLVIDAR SACAR ESTOOOO
        monto_mensual = round(random.uniform(0, 10000), 2)
        registro = Servicios(num_id, nomb_titular, tipo_cliente, tipo_producto, monto_mensual)
        add_in_order(facturas, registro)
    return facturas


'''
2 - Mostar el contenido del vector a razón de un registro por línea
'''


def mostrar(facturas):
    for factura in facturas:
        print(factura)


'''
3 - Buscar una factura con numero de identificación X,
   donde X se carga por teclado. Si existe mostrar sus datos, caso contrario indicar con un mensaje
'''


def buscar_arreglo(facturas):
    nom = int(input('Ingrese número de identificación de la factura:'))
    for i in range(len(facturas)):
        if facturas[i].num_id == nom:
            print(facturas[i])
        else:
            print('No hay coincidencias')


'''
4 - A partir del arreglo del punto 1, generar una matriz por tipo de cliente y tipo de producto,
    donde cada componente contenga la cantidad de clientes  (144 contadores).
    Muestre de dicha matriz solo los valores que sean mayor a cero       
'''


def cant_clientes_x_tipo_producto(facturas):
    filas = 9
    columnas = 16
    m = [[0] * columnas for f in range(filas)]
    for i in range(len(facturas)):
        m[facturas[i].tipo_cliente][facturas[i].tipo_producto] += 1

    for j in range(len(m)):
        for k in range(len(m[0])):
            if m[j][k] != 0:
                print('Tipo de cliente', j, ' Tipo de producto : ', k, ' : ', m[j][k])


'''
5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo X ingresado por parámetro y
   que su tipo de producto no sean ni 2, 3 o 4. 
   Muestre los registros de ese archivo y al final indique cual fue el total facturado para todos esas facturas
'''


def generar_archivo(facturas, nombre_archivo, x):
    f = open(nombre_archivo, 'wb')  # Abre el archivo si existe y si lo crea
    for factura in facturas:
        if ((factura.tipo_producto != 2 or factura.tipo_producto != 3 or factura.tipo_producto != 4)) and (
                factura.tipo_cliente == x):
            pickle.dump(factura, f)
    f.close()
    print('Archivo creado !')


def mostrar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        f = open(nombre_archivo, 'rb')
        size = os.path.getsize(nombre_archivo)
        total_facturado = 0
        while f.tell() < size:
            reg = pickle.load(f)
            total_facturado += reg.monto_mensual
            print(reg)
        f.close()
        print('Total facturado para todas esas facturas es de: $', total_facturado)
    else:
        print('El archivo', nombre_archivo, 'esta vacío')


def validar_cliente(facturas, x):
    for factura in facturas:
        if factura.tipo_cliente == x:
            return 1
    return -1


'''
6 - A partir del arreglo, para un tipo de producto X que se ingresa por teclado, informar cual fue el total facturado
    y que porcentaje representa sobre el total de facturas del arreglo.
'''


def porcentaje_total(facturas, producto):
    total_facturado_prod = 0  # suma total de productos
    total = 0  # suma todos los productos
    for factura in facturas:
        if factura.tipo_producto == producto:
            total_facturado_prod += factura.monto_mensual
        total += factura.monto_mensual
    print('Total facturado para el producto', producto, ':  $', total_facturado_prod)
    porcentaje = ((total_facturado_prod / total) * 100)
    print('TOTAL --> ', total)
    print('El porcentaje obtenido es: ', porcentaje, '% ')


def validar_n(inf, mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ', inf, ':')
        n = int(input())
    return n


def principal():
    
    opcion = -1
    nombre_archivo = 'Registros.dat'
    while opcion != 0:
        print(50 * '-')
        print('MENÚ DE OPCIONES: ')
        print('PROVEEDORA DE SERVICIO DE INTERNET')
        print(50 * '-')
        print('1. Cargar automaticamente')
        print('2. Mostrar ')
        print('3. Buscar número identificación de la factura')
        print('4. Cantidad de clientes por tipo de cliente y tipo de producto ')
        print('5. Archivo con facturas ')
        print('6. Total facturado')
        print('0. Salir')

        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            
            facturas = []
            n = validar_n(0, "Ingrese la cantidad de facturas: ")
            facturas = carga_automatica(facturas, n)
            print('Se creo uno nuevo')
        else:
            if len(facturas) == 0:
                print('Debe ingresar la opcion 1.')
            elif opcion == 2:
                mostrar(facturas)
            elif opcion == 3:
                buscar_arreglo(facturas)
            elif opcion == 4:
                cant_clientes_x_tipo_producto(facturas)
            elif opcion == 5:
                x = validar_n(0, 'Ingrese número de cliente: ')
                cliente = validar_cliente(facturas, x)
                if cliente == 1:
                    generar_archivo(facturas, nombre_archivo, x)
                    mostrar_archivo(nombre_archivo)
                else:
                    print('Este cliente no existe!')
            elif opcion == 6:
                producto = validar_n(0, 'Ingrese tipo de producto: ')
                porcentaje_total(facturas, producto)

            elif opcion == 7:
                print('Hasta luego!! :)')


if __name__ == '__main__':
    principal()
