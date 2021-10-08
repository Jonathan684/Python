import os
import pickle
from registro import * 
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

6 - A partir del arreglo, para un tipo de producto X que se ingresa por teclado informar cual fue el total facturado
    y que porcentaje representa sobre el total de facturas del arreglo.
'''



'''
    1 - Cargar un vector de n facturas, validando todos los posibles valores,
   la carga puede ser manual, automática, o bien puede implementar ambas. 
   El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado por numero de identificación

'''
def add_in_order(facturas, registro):
    izq, der = 0, len(facturas)-1
    while izq <= der :
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


def carga_automatica(facturas,n):
   nombre_titular = ['Jonathan', 'Candela', 'Nadia', 'Matías']
   for i in range(n):
      num_id = i
      nomb_titular = random.choice(nombre_titular)
      tipo_cliente = round(random.uniform(0,10000),2)
      tipo_producto = random.randint(0, 8) ## NO OLVIDAR SACAR ESTOOOO 
      monto_mensual = random.randint(0, 15)
      registro = Servicios(num_id, nomb_titular, tipo_cliente, tipo_producto, monto_mensual)
      add_in_order(facturas, registro)
      ##facturas[i] = Servicios(numero_identificacion, nomb_titular, tipo_cliente, tipo_producto, monto_mensual)
   return facturas 
'''
2 - Mostar el contenido del vector a razón de un registro por línea
'''
def mostrar(facturas):
    for i in range(len(facturas)):
        print(facturas[i])
        

def validar_n(inf, mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ' , inf, ':')  
        n = int(input())
    return n

def principal():
    facturas = list() 
    opcion = -1
    nom_arch= 'Registros.dat'
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
            n = validar_n(0,"Ingrese la cantidad de facturas: ")
            #facturas = n * [0]
            facturas = carga_automatica(facturas,n)
        else:
            if len(facturas) == 0:
                print('Debe ingresar la opcion 1.')  
            elif opcion == 2 :
                mostrar(facturas)
            elif opcion == 3:
                pass
                #x = validar_n(0,'Ingrese importe del medicamento: ') 
                #generar_archivo(facturas, nom_arch,x )
            elif opcion == 4:
                pass
                #mostrar_archivo(nom_arch)
            elif opcion == 5:
                pass
                #buscar_arreglo(facturas)
            elif opcion == 6:
                pass
                #cant_med_x_present(facturas)            
if __name__ == '__main__':
    principal() 